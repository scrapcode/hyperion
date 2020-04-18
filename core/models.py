from enum import Enum

from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


def django_enum(cls):
    """ Decorator to enable enums in django templates
    """
    cls.do_not_call_in_templates = True
    return cls


@django_enum
class StatusChoices(Enum):
    """ Provides a nice way of allowing choices in the status field.
    """
    PENDING = "Pending"
    ACTIVE = "Active"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"

    @classmethod
    def choices(cls):
        """Returns all options in the StatusChoices enum
        """
        return [(key.value, key.name) for key in cls]

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Project(models.Model):
    """ The base model for all projects. Projects can be used for explicit project or
    as groups for generic but related Tasks.
    """
    name = models.CharField(max_length=256)
    code = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)
    status = models.CharField(max_length=128,
                              choices=StatusChoices.choices(),
                              default=StatusChoices.ACTIVE)
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

    @property
    def active_tasks(self):
        """Returns all project tasks with a status of 'Active'
        """
        active_tasks = self.tasks.filter(status=StatusChoices.ACTIVE.value)
        return active_tasks

    def get_absolute_url(self):
        """Return the URL to the Project's details page.
        """
        return reverse("project_detail", kwargs={"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.code)
        return super().save(force_insert=force_insert,
                            force_update=force_update,
                            using=using,
                            update_fields=update_fields)

    def __str__(self):
        return self.name


class Task(models.Model):
    """ The base model for all Tasks. Tasks can be standalone or belong to a project.
    Tasks can be followups to parent tasks.
    """
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
        related_name='tasks',
        blank=True,
        null=True
    )
    status = models.CharField(max_length=128,
                              choices=StatusChoices.choices(),
                              default=StatusChoices.PENDING)
    followup_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name="followups",
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def is_followup(self):
        """Returns True if this Task is a followup to another Task.
        """
        return self.followup_to is not None

    def __str__(self):
        return self.name
