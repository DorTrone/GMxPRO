from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('fakultet', FakultetViewSet)
router.register('kafedra', KafedraViewSet)
router.register('courses', CourseViewSet)
router.register('groups', GroupViewSet)
router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('status', StatusViewSet, basename='status')
router.register('gelmedi', GelmediViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
