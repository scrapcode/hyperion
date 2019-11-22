from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta

from .models import Followup

class FollowupManagerTest(TestCase):
    _testUser = User()

    def setUp(self):
        self._testUser = User.objects.create_user(username='testUser', password='12345')

        Followup.objects.create(
            description="one",
            send_date=(timezone.now()-timedelta(days=10)),
            user = self._testUser,
        )
        Followup.objects.create(
            description="two",
            send_date=(timezone.now()-timedelta(days=5)),
            user = self._testUser,
        )
        Followup.objects.create(
            description="three",
            send_date=(timezone.now()+timedelta(days=5)),
            user = self._testUser,
        )
        Followup.objects.create(
            description="four",
            send_date=(timezone.now()+timedelta(days=10)),
            user = self._testUser,
        )


    def test_get_overdue_followups(self):
        overdue_followups = Followup.objects.overdue()
        self.assertEqual(overdue_followups.count(), 2)

    def test_get_overdue_followups_with_user(self):
        overdue_followups = Followup.objects.overdue(self._testUser)
        self.assertEqual(overdue_followups.count(), 2)

    def test_get_upcoming_followups(self):
        upcoming_followups = Followup.objects.upcoming(self._testUser, 7)
        self.assertEqual(upcoming_followups.count(), 1)

        upcoming_followups = Followup.objects.upcoming(self._testUser, 12)
        self.assertEqual(upcoming_followups.count(), 2)