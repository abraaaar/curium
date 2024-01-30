# five/models.py

from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Default Name')
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True)



    def __str__(self):
        return self.name

class UserQualifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    education = models.CharField(max_length=255, default='', blank=True)  # Updated max_length
    hobbies = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Qualifications"
