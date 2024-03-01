from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.timezone import now

from userAuth.models import Person


class Faculty(models.Model):
    username = models.CharField(max_length=10,unique=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    first_name = models.CharField(max_length=50,null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.username = f"F{self.date_of_birth.strftime("%Y")}{self.first_name}"
        password = self.date_of_birth.strftime("%Y-%m-%d")
        user=User.objects.create_user(username=self.username, password=password)
        self.user=user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation}"

class Program(models.Model):
    program_name=models.CharField(max_length=100)
    department_name=models.CharField(max_length=20)
    program_duration=models.FloatField()

class Exam(models.Model):
    program=models.ForeignKey(Program,on_delete=models.CASCADE)
    exam_type=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    duration=models.DurationField()
    program_name=models.CharField(max_length=100)
    totalmarks = models.DecimalField(max_digits=10,decimal_places=2)
    passingmark = models.DecimalField(max_digits=10,decimal_places=2)
    semester = models.DecimalField(max_digits=10,decimal_places=2)

class ExamPaper(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)

class Subject(models.Model):
    subjectcode=models.CharField(max_length=20)
    subjectname=models.CharField(max_length=20)
    program=models.ManyToManyField(Program)
    reference_book=models.CharField(max_length=20)

class Hallticket(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student=models.ForeignKey('studentPanel.Student',on_delete=models.CASCADE)
    program=models.ForeignKey(Program,on_delete=models.CASCADE)

class Mark(models.Model):
    obtained_marks=models.IntegerField()
    student=models.ForeignKey('studentPanel.Student',on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    subject=models.OneToOneField(Subject,on_delete=models.CASCADE)

class Announcement(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    time = models.DateTimeField()
    content = models.TextField(max_length=500)

class AttendanceRecord(models.Model):
    student = models.ForeignKey('studentPanel.Student', on_delete=models.CASCADE)
    total_hours = models.IntegerField(null=True, blank=True)
    present_hours = models.IntegerField(null=True, blank=True)
    upload_date = models.DateField(default=now())
    models.CheckConstraint(check=Q(total_hours__gte=present_hours), name='total_hours greater than present_hours')

