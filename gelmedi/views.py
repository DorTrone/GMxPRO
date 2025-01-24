from rest_framework import viewsets
from .models import *
from .serializers import *

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

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class GelmediViewSet(viewsets.ModelViewSet):
    queryset = Gelmedi.objects.all()
    serializer_class = GelmediSerializer