# Generated by Django 3.0.6 on 2020-10-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_application_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='sem',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=5),
        ),
    ]
