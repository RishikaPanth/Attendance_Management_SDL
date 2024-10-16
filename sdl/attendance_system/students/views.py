
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import StudentRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .form import LoginForm
from .models import Student , User ,Attendance, SubjectAttendance

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
             # Check if the username already exists
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'register.html', {'form': form})

            # Check if the email already exists in the User model
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'register.html', {'form': form})

            # Save user first
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']  # Set the user's email
            user.save()  # Save the user instance

           
            student = Student.objects.create(
                user=user,  # Link the user to the student
                batch=form.cleaned_data.get('batch'),
                branch=form.cleaned_data.get('branch'),
                enrollment_no=form.cleaned_data.get('enrollment_no'),
                semester=form.cleaned_data.get('semester'),
                email=form.cleaned_data['email'] 
            )
            student.save()


            # Log the user in after registration
            login(request, user)
            print("User registered successfully")  # Debugging
            return redirect('home')
        else:
            print("Form errors:", form.errors)  # Debugging
           
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']  # Get the roll number from the form
        password = request.POST['password']
        
        try:
            # Get the student by roll number
            student = Student.objects.get(enrollment_no=roll_no)
            user = authenticate(request, username=student.user.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')  # Redirect to the dashboard after successful login
            else:
                messages.error(request, 'Invalid roll number or password.')
        except Student.DoesNotExist:
            messages.error(request, 'Student with this roll number does not exist.')
    
    return render(request, 'login.html')  # Render the login page


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)

    # Get all SubjectAttendance records for the student
    subject_attendance_records = SubjectAttendance.objects.filter(attendance__student=student)

    # Prepare attendance data for each subject
    attendance_data = []
    for record in subject_attendance_records:
        total_classes = record.total_classes
        present_classes = record.present_classes
        attendance_percentage = (present_classes / total_classes * 100) if total_classes > 0 else 0

        attendance_data.append({
            'subject': record.subject.name,  # Assuming the Subject model has a 'name' field
            'attendance_percentage': attendance_percentage,
        })

    context = {
        'student': student,
        'attendance_data': attendance_data,
    }
    return render(request, 'students/student_dashboard.html', context)
