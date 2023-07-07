from django import forms
from .models import Student, Carrer, Enrollment, Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['dni', 'first_last_name', 'second_last_name', 'first_name', 'middle_name', 'date_of_birth', 'genre', 'validity', 'carrer']

class CarrerForm(forms.ModelForm):
    class Meta:
        model = Carrer
        fields = ['code', 'name', 'duration']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'credits', 'professor']

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user