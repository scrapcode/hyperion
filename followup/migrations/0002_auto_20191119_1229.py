# Generated by Django 2.2.6 on 2019-11-19 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delete_followup'),
        ('followup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Task'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='send_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 3, 18, 29, 50, 158069, tzinfo=utc)),
        ),
    ]