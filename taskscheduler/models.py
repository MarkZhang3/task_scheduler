from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.TextField()
    text = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    completed = models.BooleanField()

    def __str__(self):
        return self.text


class AppPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    app_password = models.TextField(null=True, blank=True)