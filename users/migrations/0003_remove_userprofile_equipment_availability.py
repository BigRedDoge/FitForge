# Generated by Django 4.2.7 on 2023-11-28 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_workout_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='equipment_availability',
        ),
    ]