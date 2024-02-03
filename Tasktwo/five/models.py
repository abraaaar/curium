# django_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, default = 'Not Specified')
    age = models.IntegerField(blank = True, null=True, default=0)
    gender = models.CharField(max_length=255, null=True, default='Not Specified', blank = True)
    address = models.TextField(blank=True, null=True)
    step_counter = models.IntegerField(default=0)
    status_completed = models.BooleanField(default=False) 
    def __str__(self):
        return self.name

class UserQualifications(models.Model):
    user_details = models.OneToOneField(UserDetails, on_delete=models.CASCADE, related_name='qualifications')
    education = models.CharField(max_length=255, blank=True, null=True, default = 'Not Specified')
    hobbies = models.TextField(blank=True, null=True, default = 'Not Specified')
    step_counter = models.IntegerField(default=0)
    status_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Qualifications for {self.user_details.name}"

@receiver(post_save, sender=UserDetails)
def create_user_qualifications(sender, instance, created, **kwargs):
    if created:
        UserQualifications.objects.create(user_details=instance)