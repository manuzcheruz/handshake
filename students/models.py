from django.db import models
from centers.models import *

# Create your models here.
# campus profile
# the 
class Student(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    course = models.CharField(max_length=500)
    year = models.CharField(max_length=50)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name


class Semester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.name
