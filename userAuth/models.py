from django.db import models

# Create your models here.
class User(models.Model):
    username = models.Count(max_length=12)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
