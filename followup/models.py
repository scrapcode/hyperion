from django.db import models
from django.contrib.auth.models import User

from core.models import Project, Task
from .helpers import two_weeks_from_today


class Followup(models.Model):
    description = models.CharField(max_length=256)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followups')

    send_date = models.DateField(default=two_weeks_from_today(), blank=False, null=False)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    task = models.ForeignKey(Task, on_delete=models.SET_NULL, blank=True, null=True)