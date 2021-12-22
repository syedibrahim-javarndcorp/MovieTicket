from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    seats = models.IntegerField(null=True,blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    payment = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title