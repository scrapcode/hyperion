from django.db import models
from django.contrib.auth.models import User
from core.models import Project

class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')