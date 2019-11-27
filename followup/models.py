from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import timedelta

from core.models import Project, Task
from .helpers import two_weeks_from_today


class FollowupManager(models.Manager):

    def overdue(self, user=None):
        """
        overdue
        Calculated as any date before timezone.now()
        """
        today = timezone.now()

        if user:
            return self.filter(send_date__lt=today, is_completed=False, user=user)

        return self.filter(send_date__lt=today, is_completed=False)


    def upcoming(self, user=None, threshold=7):
        """
        upcoming
        Calculated from timezone.now() until (now + threshold) in days.
        """
        today = timezone.now()
        threshold_date = timezone.now() + timedelta(days=threshold)

        if user:
            return self.filter(send_date__range=(today, threshold_date), is_completed=False, user=user)

        return self.filter(send_date__range=(today, threshold_date), is_completed=False)


class Followup(models.Model):

    description = models.CharField(max_length=256)
    
    user = models.ForeignKey(User,
        on_delete=models.CASCADE, 
        related_name='followups'
    )

    send_date = models.DateField(
        default=two_weeks_from_today(),
        blank=False,
        null=False
    )

    is_completed = models.BooleanField(default=False)

    project = models.ForeignKey(Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    task = models.ForeignKey(Task,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    objects = FollowupManager()