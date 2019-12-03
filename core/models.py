from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

from enum import Enum


def django_enum(cls):
    # decorator to enable enums in django templates
    cls.do_not_call_in_templates = True
    return cls


@django_enum
class StatusChoices(Enum):
    PENDING = "Pending"
    ACTIVE = "Active"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Project(models.Model):

    name = models.CharField(max_length=256)
    code = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)
    status = models.CharField(max_length = 128, choices=StatusChoices.choices(), default=StatusChoices.ACTIVE)
    completion_date = models.DateField(blank=True, null=True)
    point_of_contact = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects_created'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=False, null=False)

    def active_tasks(self):
        t = self.tasks.filter(status=StatusChoices.ACTIVE)
        return t

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.code)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    status = models.CharField(max_length = 128, choices=StatusChoices.choices(), default=StatusChoices.PENDING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
