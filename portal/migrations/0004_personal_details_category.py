# Generated by Django 3.0.6 on 2020-10-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_personal_details_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='category',
            field=models.IntegerField(choices=[(1, 'OPEN'), (2, 'OBC'), (3, 'SC'), (4, 'ST'), (5, 'VJNT')], default=1),
        ),
    ]
