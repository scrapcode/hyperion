from django.contrib import admin
from .models import Followup

class FollowupAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register(Followup, FollowupAdmin)