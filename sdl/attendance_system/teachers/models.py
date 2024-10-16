

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from students.models import Student 

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class TeacherAccess(models.Model):
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Teacher Access Password"
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teacher_attendance')
    batch = models.CharField(max_length=10, default='Unknown Batch')  # Store student's batch
    enrollment_no = models.CharField(max_length=15, default='Unknown Enrollment')  # Store student's enrollment number
    attendance_percentage = models.FloatField(default=0)  # Store attendance percentage

    

    def __str__(self):
        return f"{self.student} - {self.enrollment_no} - {self.attendance_percentage}%"