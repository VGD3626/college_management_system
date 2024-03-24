from django.contrib.auth.models import User
from django.db import models
from studentPanel.models import Student
from facultyPanel.models import Faculty


class Hod(models.Model):
    username = models.CharField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.username = f"AC{self.date_of_birth.strftime("%Y")}{self.first_name}"
        password = self.date_of_birth.strftime("%Y-%m-%d")
        user = User.objects.create_user(username=self.username, password=password)
        self.user = user
        super().save(*args, **kwargs)

class Event(models.Model):
    eventID=models.IntegerField()
    eventname=models.CharField(max_length=100)
    hod=models.ManyToManyField(Hod)
    description=models.TextField()
    starttime=models.DateField()
    duration=models.DurationField()

class Club(models.Model):
    clubid=models.IntegerField()
    clubname=models.CharField(max_length=100)
    hod=models.ManyToManyField(Hod)
    student=models.ManyToManyField(Student)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    estdate=models.DateField()
    type=models.CharField(max_length=100)
