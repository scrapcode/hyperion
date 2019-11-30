# Generated by Django 2.2.6 on 2019-11-30 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections', to=settings.AUTH_USER_MODEL),
        ),
    ]