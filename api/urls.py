from django.urls import path
from . import views

urlpatterns = [
    path("",views.getroutes),
    path('movie/',views.getmovie),
]