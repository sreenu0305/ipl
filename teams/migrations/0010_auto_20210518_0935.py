# Generated by Django 3.1.7 on 2021-05-18 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20210518_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='team_one',
            new_name='team1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='team_two',
            new_name='team2',
        ),
    ]
