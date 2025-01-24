from django.contrib import admin
from .models import *


@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course__name')
    list_filter = ('course',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group', 'phone', 'par_phone')
    search_fields = ('full_name', 'group__name')
    list_filter = ('group',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'kafedra')
    search_fields = ('full_name', 'kafedra', 'login')
    list_filter = ('fakultet', 'kafedra')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Gelmedi)
class GelmediAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'date')
    search_fields = ('student', 'date', 'status')