# Generated by Django 5.1.1 on 2024-10-02 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='present_classes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='total_classes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]
