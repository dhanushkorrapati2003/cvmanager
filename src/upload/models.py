from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_size
import os 


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.username
    
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/', validators=[validate_file_size])
    timestamp = models.DateTimeField(auto_now_add=True)
    skills = models.CharField(max_length=1000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        # First, delete the associated resume file
        if self.resume:
            if os.path.isfile(self.resume.path):
                os.remove(self.resume.path)
        
        super(Person, self).delete(*args, **kwargs)
    class Meta:
        ordering = ['first_name']
    
        
class AuditLog(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    before = models.CharField(max_length=255) # Before the action  
    after = models.CharField(max_length=255)  # After the action
