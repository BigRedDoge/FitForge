# Generated by Django 4.2.7 on 2023-11-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='workout_duration',
            field=models.IntegerField(default=0),
        ),
    ]