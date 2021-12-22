from django.urls import path
from . import views

urlpatterns = [
    path("",views.getroutes),
    path('movie/',views.getmovies),
    path('movie/<str:pk>',views.getmovie),

]