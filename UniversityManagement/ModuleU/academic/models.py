from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Carrer(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveBigIntegerField(default=5)

    def __str__(self) -> str:
        txt = f'Name: {self.name} (duration: {self.duration} years)'
        return txt

class Student(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    dni = models.CharField(max_length=8, unique=True)
    first_last_name = models.CharField(max_length=35)
    second_last_name = models.CharField(max_length=35)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    gen = [
        ('F', 'Female'), 
        ('M', 'Male')
    ]
    genre = models.CharField(max_length=1, choices=gen, default='F')
    validity = models.BooleanField(default=True)
    carrer = models.ForeignKey(Carrer, null=False, blank=False, on_delete=models.CASCADE)

    def completeName(self):
        txt = "{0} {1}, {2} {3}"
        return txt.format(self.first_last_name, self.second_last_name, self.first_name, self.middle_name)
    
    def __str__(self) -> str:
        if self.validity:
            stateStudent = "VALIDATED"
        else:
            stateStudent = "NOT VALIDATED"
        txt = f'{self.completeName()} / Carrera: {self.carrer.name}/ {stateStudent}'
        return txt

class Course(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=40)
    credits = models.PositiveBigIntegerField()
    professor = models.CharField(max_length=100)

    def __str__(self) -> str:
        txt = f'{self.name} ({self.code}) / Professor: {self.professor}'
        return txt

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        txt = f'{self.student.completeName()} registered to the course {self.course.name} / Professor: {self.course.professor} / Date: {self.pub_date}'
        return txt
