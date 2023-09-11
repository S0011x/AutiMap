from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Request(models.Model):
    time_choices =(('8:00','8:00 am'),('9:00','9:00 am'),('10:00','10:00 am'),('11:00','11:00 am'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    times = models.CharField(max_length=128, choices= time_choices)