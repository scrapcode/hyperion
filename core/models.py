from django.db import models
from django.contrib.auth.models import User
from .helpers import two_weeks_from_today

"""
Project
"""
class Project(models.Model):
    ACTIVE = 'AC'
    COMPLETE = 'CL'
    CANCELLED = 'CA'

    LIST_OF_CHOICES = [
        (ACTIVE, 'Active'),
        (COMPLETE, 'Completed'),
        (CANCELLED, 'Cancelled')
    ]

    name = models.CharField(max_length=256)
    code = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=LIST_OF_CHOICES,
        default=ACTIVE
    )

    point_of_contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

"""
Task
"""
class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name + ' (' + project.name + ')'

"""
Followup
"""
class Followup(models.Model):
    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followups')
    send_date = models.DateField(default=two_weeks_from_today(), blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)