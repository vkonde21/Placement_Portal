# Generated by Django 3.0.6 on 2020-10-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_shortlisted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortlisted',
            name='id',
        ),
        migrations.AddField(
            model_name='shortlisted',
            name='r_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
