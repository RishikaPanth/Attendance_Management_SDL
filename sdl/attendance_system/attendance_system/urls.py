"""
URL configuration for attendance_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students import views as student_views 
from teachers import views as teacher_views
from students.views import student_dashboard ,student_login
from teachers import views
from teachers.views import mark_attendance ,teacher_dashboard_view



urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', student_views.register, name='student_register'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
  
    path('enter-password/',teacher_dashboard_view, name='enter_password'),  # For password entry
    path('dashboard/', teacher_views.teacher_dashboard, name='teacher_dashboard'),
   
     path('login/', student_login, name='login'),
      path('mark-attendance/', mark_attendance, name='mark_attendance'),
    path('export_attendance_excel/<int:semester>/', views.export_attendance_excel, name='export_attendance_excel'),
]
