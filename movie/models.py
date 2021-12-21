from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
