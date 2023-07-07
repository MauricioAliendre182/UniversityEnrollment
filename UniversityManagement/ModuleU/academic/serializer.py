from rest_framework import serializers
from .models import Enrollment, Course, Student, Carrer
from rest_framework_simplejwt.tokens import RefreshToken

class CarrerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrer
        fields = ['id','code', 'name', 'duration']

class StudentSerializer(serializers.ModelSerializer):
    carrer = serializers.PrimaryKeyRelatedField(queryset=Carrer.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'dni', 'first_last_name', 'second_last_name', 'first_name', 'middle_name', 'date_of_birth', 'genre', 'validity', 'carrer']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'name', 'credits', 'professor']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all()) 
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all()) 

    class Meta:
        model = Enrollment
        fields = ['id', 'pub_date', 'student', 'course']
