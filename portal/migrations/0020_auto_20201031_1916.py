# Generated by Django 3.0.6 on 2020-10-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20201031_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='post',
            field=models.TextField(default='', help_text='Enter the post', max_length=2000),
        ),
    ]