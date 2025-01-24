from rest_framework import viewsets
from .models import Fakultet, Kafedra, Student, Group, Course, Teacher, Status
from .serializers import StudentSerializer, GroupSerializer, CourseSerializer, KafedraSerializer, FakultetSerializer, TeacherSerializer

class FakultetViewSet(viewsets.ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer

class KafedraViewSet(viewsets.ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer