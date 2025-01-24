from rest_framework import serializers
from .models import *

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']
class KafedraSerializer(serializers.ModelSerializer):
    fakultet = FakultetSerializer()
    class Meta:
        model = Kafedra
        fields = ['id', 'name', 'fakultet']

class TeacherSerializer(serializers.ModelSerializer):
    kafedra = KafedraSerializer()
    fakultet = FakultetSerializer()
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'phone', 'password', 'kafedra', 'fakultet', 'login']


class KafedraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class GroupSerializer(serializers.ModelSerializer):
    course = CourseSerializer() 
    kafedra = KafedraSerializer()
    class Meta:
        model = Group
        fields = ['id', 'name', 'course', 'kafedra', 'spec']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    # status - StatusSerializer()
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'phone', 'group']
class GelmediSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    teacher = TeacherSerializer()
    class Meta:
        model = Gelmedi
        fields = ['id', 'student', 'teacher', 'status', 'date']
