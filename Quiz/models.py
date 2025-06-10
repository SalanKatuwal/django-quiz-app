from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Quiz(models.Model):
    DIFFICULTY_CHOICES =[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ]
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100,choices=DIFFICULTY_CHOICES)
    
    def __str__(self):
        return self.question
    
class score(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    score = models.IntegerField()
    
class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    
class EmailOtp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)