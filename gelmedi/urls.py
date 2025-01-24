from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, GroupViewSet, CourseViewSet, KafedraViewSet, FakultetViewSet

router = DefaultRouter()
router.register('fakultet', FakultetViewSet)
router.register('kafedra', KafedraViewSet)
router.register('courses', CourseViewSet)
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
