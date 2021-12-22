from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Movies


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"