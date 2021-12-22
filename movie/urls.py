from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_info/', views.userdata, name='userdata'),
    path('book-ticket/',views.bookticket, name='bookticket'),
]
