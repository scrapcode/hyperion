from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Project, ProjectAdmin)