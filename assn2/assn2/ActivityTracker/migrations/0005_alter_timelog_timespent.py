# Generated by Django 5.1.1 on 2024-09-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityTracker', '0004_timelog_timespent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelog',
            name='timeSpent',
            field=models.TextField(),
        ),
    ]