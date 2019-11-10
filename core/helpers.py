from django.db import models
from django.utils import timezone
from datetime import timedelta


def two_weeks_from_today():
    return timezone.now() + timedelta(days=14)