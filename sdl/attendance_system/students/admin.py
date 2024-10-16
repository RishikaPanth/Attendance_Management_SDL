from django.contrib import admin
from .models import Student, Attendance, Subject
from students.models import SubjectAttendance


# Customize the admin to display important fields
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'batch', 'branch', 'enrollment_no', 'semester')

admin.site.register(Student, StudentAdmin)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_classes', 'present_classes', 'overall_attendance_percentage')

@admin.register(SubjectAttendance)
class SubjectAttendanceAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'subject', 'total_classes', 'present_classes', 'attendance_percentage')
    list_filter = ('subject',)  # Enables filtering by subject
    search_fields = ('attendance__student__enrollment_no', 'attendance__student__user__username')  # Optional for searching students
    
    # This method calculates attendance percentage
    def attendance_percentage(self, obj):
         if obj.total_classes > 0:
            # Format to 2 decimal places
            return "{:.2f}".format((obj.present_classes / obj.total_classes) * 100)
         return "0.00"
    attendance_percentage.short_description = 'Attendance Percentage'


admin.site.register(Subject)