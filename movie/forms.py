from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Movies
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

# class CustUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = 