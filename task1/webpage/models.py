# models.py
from django.db import models
from django.contrib.auth.models import User

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="receipe")
