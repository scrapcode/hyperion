from enum import Enum

from django.db import models
from django.contrib.auth.models import User


class FrequencyChoices(Enum):

    WEEK = "Weekly"
    MONTH = "Monthly"
    BIANNUAL = "Bi-annual"
    ANNUAL = "Annual"
    BIENNIAL = "Biennial"
    FIVE_YEAR = "Five-year"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)




class StatusChoices(Enum):

    PENDING = "Pending"
    ACTIVE = "Active"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Inspection(models.Model):

    title = models.CharField(max_length=128)
    frequency = models.CharField(
        max_length=32,
        choices=FrequencyChoices.choices(),
        default=FrequencyChoices.WEEK
    )
    status = models.CharField(
        max_length=32,
        choices=StatusChoices.choices(),
        default=StatusChoices.PENDING
    )

    date_last_completed = models.DateField(blank=True, null=True)
    date_next_due = models.DateField(blank=False,null=False)

    procedure = models.TextField(blank=False, null=False)

    estimated_cost = models.FloatField(default=0.00, blank=False, null=False)

    assigned_to = models.ForeignKey(
        User,
        related_name='inspections',
        on_delete=models.SET_NULL,
        null=True
    )