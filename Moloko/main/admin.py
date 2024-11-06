from django.contrib import admin

from .models import Project, Task, TaskHistory, Profile, Employee

# Register your models here.
admin.site.register(Project),
admin.site.register(Task),
admin.site.register(TaskHistory),
admin.site.register(Profile)
admin.site.register(Employee)