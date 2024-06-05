from django.contrib import admin
from .models import Project,ProjectVersion,ProjectMember
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectVersion)
admin.site.register(ProjectMember)