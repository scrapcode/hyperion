from django.db import models
from django.contrib.auth.models import User


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

    completion_date = models.DateField(blank=True, null=True)

    point_of_contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # todo: if determined to be beneficial, throw a ValidationError / warning on save when
    #       project is set to "complete" but does not have a completion date.
    
    def __str__(self):
        return self.name


class Task(models.Model):
    ACTIVE = 'AC'
    COMPLETE = 'CL'
    CANCELLED = 'CA'

    LIST_OF_CHOICES = [
        (ACTIVE, 'Active'),
        (COMPLETE, 'Completed'),
        (CANCELLED, 'Cancelled')
    ]

    name = models.CharField(max_length=256)
    description = models.TextField(blank=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    status = models.CharField(
        max_length=2,
        choices=LIST_OF_CHOICES,
        default=ACTIVE
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
