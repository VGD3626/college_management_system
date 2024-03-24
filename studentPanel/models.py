from django.db import models
from django.contrib.auth.models import User
from facultyPanel.models import Program

class Student(models.Model):

    username=models.CharField(max_length=50,unique=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    first_name = models.CharField(max_length=50,null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50,null=True)
    house_no = models.CharField(max_length=20, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    area_landmark = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    program_name = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True)
    roll_no = models.CharField(max_length=50,null=True)
    program=models.ForeignKey(Program,on_delete=models.CASCADE,null=True)
    degree = models.CharField(max_length=100,null=True)
    batch_year = models.IntegerField()
    semester = models.IntegerField()

    def save(self, *args, **kwargs):
        self.username = f"S{self.date_of_birth.strftime("%Y")}{self.program_name}{self.first_name}"
        password = self.date_of_birth.strftime("%Y-%m-%d")
        user=User.objects.create_user(username=self.username, password=password)
        self.user=user
        super().save(*args,**kwargs)