# Generated by Django 2.2.6 on 2019-11-30 18:34

from django.db import migrations, models
import inspections.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_auto_20191130_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='frequency',
            field=models.CharField(choices=[('WEEK', 'Weekly'), ('MONTH', 'Monthly'), ('BIANNUAL', 'Bi-annual'), ('ANNUAL', 'Annual'), ('BIENNIAL', 'Biennial'), ('FIVE_YEAR', 'Five-year')], default=inspections.models.FrequencyChoices('Weekly'), max_length=32),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('COMPLETE', 'Complete'), ('CANCELLED', 'Cancelled')], default=inspections.models.StatusChoices('Pending'), max_length=32),
        ),
    ]
