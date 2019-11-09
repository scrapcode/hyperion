from django.db import models
from django.contrib.auth.models import User
from core.models import Project
from datetime import timedelta, timezone

def two_weeks_from_today():
    return timezone.now() + timedelta(days=14)

class Followup(models.Model):
    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followups')
    send_date = models.DateField(default=two_weeks_from_today(), blank=False, null=False)