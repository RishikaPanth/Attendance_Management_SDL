# Generated by Django 5.1.1 on 2024-10-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='batch',
            field=models.CharField(default='Unknown Batch', max_length=10),
        ),
        migrations.AddField(
            model_name='attendance',
            name='enrollment_no',
            field=models.CharField(default='Unknown Enrollment', max_length=15),
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='is_present',
        ),
    ]
