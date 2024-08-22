from django.contrib import admin
from .models import Task, Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass