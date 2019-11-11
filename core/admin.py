from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Project


admin.site.site_header = "Hyperion Admin"
admin.site.site_title = "Hyperion Admin"
admin.site.index_title = "Welcome to the Hyperion Administration section."

class ProjectAdmin(admin.ModelAdmin):
    exclude = ('created_by',)
    list_display = ('code', 'name', 'status', 'point_of_contact', 'created', 'updated')
    list_filter = ('status', 'created', 'point_of_contact')
    fields = (
        ('name', 'code', 'status'),
        'description',
        'point_of_contact',
    )
    search_fields = ['name', 'code']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Project, ProjectAdmin)