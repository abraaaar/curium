# django_app/models.py

from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, default = 'Not Specified')
    age = models.IntegerField(blank = True, null=True, default=0)
    gender = models.CharField(max_length=255, null=True, default='Not Specified', blank = True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserQualifications(models.Model):
    user_details = models.OneToOneField(UserDetails, on_delete=models.CASCADE, related_name='qualifications')
    education = models.CharField(max_length=255, blank=True, null=True, default = 'Not Specified')
    hobbies = models.TextField(blank=True, null=True, default = 'Not Specified')

    def __str__(self):
        return f"Qualifications for {self.user_details.name}"
