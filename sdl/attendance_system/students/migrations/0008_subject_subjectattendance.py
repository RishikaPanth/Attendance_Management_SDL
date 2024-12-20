# Generated by Django 5.1.1 on 2024-10-03 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_attendance_is_present'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_classes', models.IntegerField(default=0)),
                ('present_classes', models.IntegerField(default=0)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_attendance', to='students.attendance')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.subject')),
            ],
        ),
    ]
