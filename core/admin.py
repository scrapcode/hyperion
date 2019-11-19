from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import force_text

from .models import Project, Task


"""
Admin Declarations
"""
admin.site.site_header = "Hyperion Admin"
admin.site.site_title = "Hyperion Admin"
admin.site.index_title = "Welcome to the Hyperion Administration section."


class TaskInline(admin.StackedInline):
    model = Task
    extra = 0
    fields = ["name", "description", "status", "user", "created", "updated"]
    readonly_fields = ["created", "updated"]
    show_change_link = True


class ProjectAdmin(admin.ModelAdmin):
    exclude = ('created_by',)
    list_display = ('code', 'name', 'status', 'point_of_contact', 'created', 'updated')
    list_filter = ('status', 'created', 'point_of_contact')
    fields = (
        ('name', 'code'),
        ('status', 'completion_date'),
        'description',
        'point_of_contact',
    )
    search_fields = ['name', 'code']
    inlines = [TaskInline]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
        

class TaskAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)