from django.contrib.auth.models import User
from django.db import models
from studentPanel.models import Student


class Accountant(models.Model):
    username=models.CharField(max_length=50,unique=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_profile.jpeg')
    gender = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, null=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()

    def save(self, *args, **kwargs):
        self.username = f"AC{self.date_of_birth.strftime("%Y")}{self.first_name}"
        password = self.date_of_birth.strftime("%Y-%m-%d")
        user=User.objects.create_user(username=self.username, password=password)
        self.user=user
        super().save(*args,**kwargs)

class Payment(models.Model):
    accountant=models.ManyToManyField(Accountant)
    transID=models.CharField(max_length=100, unique=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_type = models.CharField(max_length=100)
    chequeNo=models.IntegerField(null=True)
    time=models.DateTimeField()
    bank=models.CharField(max_length=40)
    semester=models.IntegerField()
    verification_status=models.BooleanField(default=False)
    