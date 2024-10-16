from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from students.models import Student, Attendance , Subject, SubjectAttendance
from django.template.loader import get_template
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import pandas as pd
from django.http import HttpResponse
import openpyxl
from django.urls import reverse
from django.contrib import messages
from .forms import PasswordForm
from .models import TeacherAccess


def teacher_dashboard_view(request):
    print("Password view accessed")
    # Handle POST request for password submission
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            try:
                # Assuming only one TeacherAccess object exists
                teacher_access = TeacherAccess.objects.get()
                if password == teacher_access.password:
                    # Redirect to the actual teacher dashboard
                    return redirect('teacher_dashboard')  # Ensure 'teacher_dashboard' is the correct URL name
                else:
                    messages.error(request, "Invalid password.")
            except TeacherAccess.DoesNotExist:
                messages.error(request, "Access not configured.")
    else:
        form = PasswordForm()

    return render(request, 'teachers/enter_password.html', {'form': form})

def teacher_dashboard(request):

    

     # Capture selected semester, defaulting to 0 if not provided
    selected_semester = request.GET.get("semester", 0)
    # Add additional logic for fetching subjects and students
    context = {
        "selected_semester": int(selected_semester),
        # Add any other context needed like subjects and filtered students
    }
    students = Student.objects.all()
    subjects = Subject.objects.all()
    

    # Filter students based on the selection
   
    batch = request.GET.get('batch')
    subject_id = request.GET.get('subject')

    if selected_semester:
        students = students.filter(semester=selected_semester)
    if batch:
        students = students.filter(batch=batch)
    selected_subject = Subject.objects.get(id=subject_id) if subject_id else None

    # Initialize student attendance data
    student_attendance = []
    for student in students:
        attendance_record, _ = Attendance.objects.get_or_create(student=student)
        attendance_percentage = attendance_record.overall_attendance_percentage()
        # Round the attendance percentage to 2 decimal places
        attendance_percentage = round(attendance_percentage, 2)
        student_attendance.append({
            'student': student,
            'attendance_percentage': attendance_percentage,
        })

        

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        attendance_status = request.POST.get('attendance_status')  
        subject_id = request.POST.get('subject_id')

        # Check that student_id and subject_id are valid
        if not student_id and subject_id:
            messages.error(request, "Both student and subject must be selected.")
            return redirect('teacher_dashboard')

        student = get_object_or_404(Student, id=student_id)
        subject = get_object_or_404(Subject, id=subject_id)

        # Create or get the subject attendance record
        attendance_record, _ = Attendance.objects.get_or_create(student=student)
        subject_attendance, _ = SubjectAttendance.objects.get_or_create(
            attendance=attendance_record, subject=subject)

         # Prevent modification if attendance is finalized
        if subject_attendance.is_finalized:
            messages.warning(request, "Attendance for this subject and student has already been finalized.")
        else:
            # Mark attendance and finalize
            subject_attendance.total_classes += 1
            if attendance_status == 'present':
                subject_attendance.present_classes += 1
            subject_attendance.is_finalized = True  # Lock attendance
            subject_attendance.save()

            # Update overall attendance
            attendance_record.total_classes += 1
            if attendance_status == 'present':
                attendance_record.present_classes += 1
            attendance_record.save()

    context = {
        'student_attendance': student_attendance,
        'subjects': subjects,
        'selected_subject': selected_subject,
        'selected_semester': selected_semester,
    }
    return render(request, 'teachers/teacher-dashboard.html', context)

def mark_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        attendance_status = request.POST.get('attendance_status')

        # Update attendance logic here based on attendance_status
        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        attendance_record, _ = Attendance.objects.get_or_create(student=student)
        subject_attendance, _ = SubjectAttendance.objects.get_or_create(attendance=attendance_record, subject=subject)

        # Update attendance counts
        subject_attendance.total_classes += 1
        if attendance_status == 'present':
            subject_attendance.present_classes += 1
        subject_attendance.save()

        # Update overall attendance
        attendance_record.total_classes += 1
        if attendance_status == 'present':
            attendance_record.present_classes += 1
        attendance_record.save()

        # Calculate and return updated attendance percentage
        attendance_percentage = attendance_record.overall_attendance_percentage()
        
        return JsonResponse({'attendance_percentage': attendance_percentage})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def export_attendance_excel(request, semester):
     # If semester is 0 or None, export all students
    students = Student.objects.all() if not semester or semester == 0 else Student.objects.filter(semester=semester)
    # Initialize Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = f"Attendance for Semester {semester}" if semester else "Student Attendance"

    # Headers
    headers = ['Student Name', 'Enrollment No']
    subjects = Subject.objects.all()  # Get all subjects
    for subject in subjects:
        headers.append(f"{subject.name} Attendance %")

    sheet.append(headers)

     # Filter students by semester
    #students = Student.objects.filter(semester=semester)
    for student in students:
        row = [student.user.username, student.enrollment_no]
        for subject in subjects:
            try:
                subject_attendance = SubjectAttendance.objects.get(attendance__student=student, subject=subject)
                attendance_percentage = round(subject_attendance.attendance_percentage(), 2)
            except SubjectAttendance.DoesNotExist:
                attendance_percentage = "N/A"
            row.append(attendance_percentage)
        sheet.append(row)

    

    # Save workbook
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="Attendance_Semester_{semester}.xlsx"'
    workbook.save(response)
    return response


# def teacher_dashboard_view(request):
#     if request.method == 'POST':
#         form = PasswordForm(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             try:
#                 # Assuming only one TeacherAccess object exists
#                 teacher_access = TeacherAccess.objects.get()
#                 if password == teacher_access.password:
#                     # Redirect to the actual teacher dashboard
#                      return redirect('teacher_dashboard')
#                 else:
#                     messages.error(request, "Invalid password.")
#             except TeacherAccess.DoesNotExist:
#                 messages.error(request, "Access not configured.")
#     else:
#         form = PasswordForm()

#     return render(request, 'teachers/enter_password.html', {'form': form})
   

def home(request):
    return render(request, 'home.html')