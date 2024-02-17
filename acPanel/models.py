from django.db import models
from userAuth.models import Person


class Accountant(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100, unique=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()