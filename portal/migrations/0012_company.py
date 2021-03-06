# Generated by Django 3.0.6 on 2020-10-26 07:15

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20201025_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=150, unique=True)),
                ('address', models.TextField(default='', help_text='Please enter your address', max_length=300)),
                ('contact', models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('ctc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('doa', models.DateField(default=datetime.date.today)),
                ('recruitment_details', models.TextField(default='', help_text='Enter recruitment details', max_length=1000)),
                ('logo', models.ImageField(default='default.jpg', upload_to='company_logos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])),
            ],
        ),
    ]
