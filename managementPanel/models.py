from django.contrib.auth.models import User
from django.db import models
from studentPanel.models import Student
from facultyPanel.models import Faculty


class Hod(models.Model):
    # person = models.OneToOneField(Person, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_profile.jpeg')
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=50)
    date_of_birth=models.DateField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        self.username = f"M{self.joining_date.strftime("%Y")}{self.first_name}"
        password = self.joining_date.strftime("%Y-%m-%d")
        user=User.objects.create_user(username=self.username, password=password)
        self.user=user
        super().save(*args, **kwargs)


class Club(models.Model):
    clubid=models.IntegerField()
    clubname=models.CharField(max_length=100)
    hod=models.ManyToManyField(Hod)
    student=models.ManyToManyField(Student)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    estdate=models.DateField()
    type=models.CharField(max_length=100)
