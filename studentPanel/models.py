from django.db import models
from userAuth.models import Person


class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    roll_no = models.CharField(max_length=50)
    program_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    batch_year = models.IntegerField()
    admission_category = models.CharField(max_length=50)
    semester = models.IntegerField()

