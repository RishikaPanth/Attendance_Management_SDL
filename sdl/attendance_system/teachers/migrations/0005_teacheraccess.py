# Generated by Django 5.1.1 on 2024-10-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_attendance_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]