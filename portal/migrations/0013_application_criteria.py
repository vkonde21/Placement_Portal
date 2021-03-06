# Generated by Django 3.0.6 on 2020-10-27 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgpa', models.FloatField(default=0.0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Branch')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Company')),
            ],
            options={
                'unique_together': {('company', 'branch')},
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'eligible'), (2, 'not eligible'), (3, 'selected'), (4, 'not selected'), (5, 'applied'), (6, 'not applied')], default=6)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Company')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Student')),
            ],
            options={
                'unique_together': {('company', 'student')},
            },
        ),
    ]
