

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  
    email = models.EmailField(unique=True)
    batch = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    enrollment_no = models.CharField(max_length=15, unique=True)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username



class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)  # One entry per student
    total_classes = models.IntegerField(default=0)
    present_classes = models.IntegerField(default=0)

    def overall_attendance_percentage(self):
    # Check if total_classes is zero to avoid division by zero
       if self.total_classes == 0:
        return 0  # Return 0% if no classes have been recorded
       return (self.present_classes / self.total_classes) * 100


class Subject(models.Model):
    name = models.CharField(max_length=100)  # Name of the subject
    code = models.CharField(max_length=10, unique=True)  # Unique code for each subject

    def __str__(self):
        return self.name       
    
class SubjectAttendance(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='subject_attendance')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=0)
    present_classes = models.IntegerField(default=0)
    is_finalized = models.BooleanField(default=False)

    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0
        return (self.present_classes / self.total_classes) * 100

    def __str__(self):
        return f"{self.subject.name} - {self.attendance.student.user.username}"