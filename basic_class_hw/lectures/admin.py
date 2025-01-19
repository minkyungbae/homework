from django.contrib import admin
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_id', 'name', 'instructor_id', 'is_online', 'prerequisite')
