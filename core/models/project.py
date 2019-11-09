from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    point_of_contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)