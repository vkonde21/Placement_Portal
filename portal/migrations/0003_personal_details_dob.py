# Generated by Django 3.0.6 on 2020-10-23 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_personal_details_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
