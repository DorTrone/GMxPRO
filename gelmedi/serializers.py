from rest_framework import serializers
from .models import Fakultet, Kafedra, Course, Group, Student, Status, Teacher

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'phone', 'password', 'kafedra', 'fakultet']

class KafedraSerializer(serializers.ModelSerializer):
    fakultet = FakultetSerializer()
    class Meta:
        model = Kafedra
        fields = ['id', 'name', 'fakultet']

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
        fields = ['id', 'name', 'course', 'kafedra']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    # status - StatusSerializer()
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'phone', 'group', 'status', 'status_display']