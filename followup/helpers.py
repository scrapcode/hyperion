from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import timedelta

# from .models import Followup


def two_weeks_from_today():
    """ Returns current date plus one fortnight.
    """
    return timezone.now() + timedelta(days=14)


""" todo: Add e-mail support for followups.

def email_followup(Followup):
"""