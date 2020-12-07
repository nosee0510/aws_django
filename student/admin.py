from django.contrib import admin
from student.models import Student

# Register your models here.

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('id', 'name', 'major')