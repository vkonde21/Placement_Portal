# Generated by Django 3.0.6 on 2020-10-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_personal_details_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='address',
            field=models.TextField(default='', help_text='Please enter your address', max_length=300),
        ),
    ]