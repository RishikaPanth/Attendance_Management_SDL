# Generated by Django 5.1.1 on 2024-09-30 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_attendance_status_attendance_is_present'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
