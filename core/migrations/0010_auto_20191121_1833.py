# Generated by Django 2.2.6 on 2019-11-22 00:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delete_followup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'COMPLETE'), (3, 'CANCELLED'), (4, 'PENDING')], default=core.models.StatusChoices(1)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'COMPLETE'), (3, 'CANCELLED'), (4, 'PENDING')], default=core.models.StatusChoices(4)),
        ),
    ]
