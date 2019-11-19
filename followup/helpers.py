from django.db import models
from django.utils import timezone
from datetime import timedelta


def two_weeks_from_today():
    """Returns current date plus one fortnight.
    
    Fourteen Days in the future.
    """
    return timezone.now() + timedelta(days=14)