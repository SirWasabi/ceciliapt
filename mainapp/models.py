from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    user_ip = models.CharField(max_length=15)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now, primary_key=True)

    def __str__(self):
        return self.user_email
