from django.urls import path
from . import views

urlpatterns = [
    path("",views.getroutes),
    path('movie/',views.getmovies),
    path('movie/<str:pk>',views.getmovie),
    path('movie/<str:pk>/title',views.getsinglemovie),
    path('movie/delete/<str:pk>',views.deletemovie),
]