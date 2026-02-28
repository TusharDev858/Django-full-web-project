from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task
    
    
# Contact models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
