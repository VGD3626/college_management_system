from django.db import models
from CMS.models import Person


class Faculty(models.Model):

    person = models.OneToOneField(Person, to_field='user_id', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} - {self.designation}"
