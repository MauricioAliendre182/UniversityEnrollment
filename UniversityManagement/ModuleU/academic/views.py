from django.shortcuts import render, redirect
from .models import Carrer, Student, Course, Enrollment
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentForm, NewUserForm, CourseForm, EnrollmentForm, CarrerForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .serializer import CarrerSerializer, CourseSerializer, EnrollmentSerializer, StudentSerializer
import requests
from rest_framework.permissions import IsAuthenticated


username = None
password = None

def get_a_token(username, password):
    credentials = {"username": username, "password": password}
    token = requests.post('http://localhost:8000/academic/api/v1/token/', data=credentials)
    header = {'Authorization': f'Bearer {token.json()["access"]}'}
    return header

@login_required
def formContact(request):
    return render(request, "formContact.html")

@login_required
def home(request):
     return render(request, "main.html")

@login_required
def contact(request):
    if request.method == "POST":
        subject = request.POST['subjectTxt']
        message = request.POST['messageTxt']
        email_from = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        email_to = [request.POST['emailTxt']]
        send_mail(subject, message, email_from, email_to, fail_silently=False)
        return render(request, "contactSuccesful.html")
    return render(request, "formContact.html", {
        'error_message': 'The email was not sent correctly'
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("academic:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            global username
            global password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("academic:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("academic:login") 

class StudentCreateView(LoginRequiredMixin,View):
    template_name = 'student.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            carrer_pk = form.cleaned_data['carrer'].pk  # Extract the primary key value
            form.cleaned_data['carrer'] = carrer_pk  # Assign the primary key to the form data

            # Serialize the form data
            serializer = StudentSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                # Make a POST request to your API to create the student
                global username
                global password
                header = get_a_token(username, password)
                response = requests.post('http://localhost:8000/academic/api/v1/students/', data=serializer.data, headers=header)
                if response.status_code == 201:
                    # Student creation successful
                    return render(request, "studentState.html", {'message': 'Student created succesfully'})
                else:
                    # Handle API response errors
                    return render(request, "studentState.html", {'message': 'Failed to create student'})
        return render(request, self.template_name, {'form': form})

class CourseCreateView(LoginRequiredMixin,View):
    template_name = 'course.html'

    def get(self, request):
        form = CourseForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            # Serialize the form data
            serializer = CourseSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                # Make a POST request to your API to create the student
                global username
                global password
                header = get_a_token(username, password)
                response = requests.post('http://localhost:8000/academic/api/v1/courses/', data=serializer.data, headers=header)
                if response.status_code == 201:
                    # Course creation successful
                    return render(request, "courseState.html", {'message': 'Course created succesfully'})
                else:
                    # Handle API response errors
                    return render(request, "courseState.html", {'message': 'Failed to create course'})
        return render(request, self.template_name, {'form': form})


class CareerCreateView(LoginRequiredMixin,View):
    template_name = 'career.html'

    def get(self, request):
        form = CarrerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CarrerForm(request.POST)
        if form.is_valid():
            # Serialize the form data
            serializer = CarrerSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                # Make a POST request to your API to create the student
                global username
                global password
                header = get_a_token(username, password)
                response = requests.post('http://localhost:8000/academic/api/v1/career/', data=serializer.data, headers=header)
                if response.status_code == 201:
                    # Career creation successful
                    return render(request, "careerState.html", {'message': 'Career created succesfully'})
                else:
                    # Handle API response errors
                    return render(request, "careerState.html", {'message': 'Failed to create career'})
        return render(request, self.template_name, {'form': form})

class EnrollmentCreateView(LoginRequiredMixin,View):
    template_name = 'enrollment.html'

    def get(self, request):
        form = EnrollmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student_pk = form.cleaned_data['student'].pk  # Extract the primary key value
            course_pk = form.cleaned_data['course'].pk
            form.cleaned_data['student'] = student_pk  # Assign the primary key to the form data
            form.cleaned_data['course'] = course_pk

            # Serialize the form data
            serializer = EnrollmentSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                # Make a POST request to your API to create the student
                global username
                global password
                header = get_a_token(username, password)
                response = requests.post('http://localhost:8000/academic/api/v1/enrollment/', data=serializer.data, headers=header)
                if response.status_code == 201:
                    # Enrollment creation successful
                    return render(request, "enrollmentState.html", {'message': 'Enrollment created succesfully'})
                else:
                    # Handle API response errors
                    return render(request, "enrollmentState.html", {'message': 'Failed to create enrollment'})
        return render(request, self.template_name, {'form': form})

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

class CarrerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Carrer.objects.all()
    serializer_class = CarrerSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CarrerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrer.objects.all()
    serializer_class = CarrerSerializer
    permission_classes = (IsAuthenticated,)

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EnrollmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (IsAuthenticated,)