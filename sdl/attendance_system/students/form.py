from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    batch = forms.CharField(max_length=20)
    branch = forms.CharField(max_length=50)
    enrollment_no = forms.CharField(max_length=20)
    semester = forms.CharField(max_length=2)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'batch', 'branch', 'enrollment_no', 'semester']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Student.objects.create(
                user=user,
                batch=self.cleaned_data['batch'],
                branch=self.cleaned_data['branch'],
                enrollment_no=self.cleaned_data['enrollment_no'],
                semester=self.cleaned_data['semester']
            )
           
        return user
    

 

class LoginForm(forms.Form):
   
    enrollment_no = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)






