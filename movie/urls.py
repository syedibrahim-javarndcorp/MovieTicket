from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_info/', views.userdata, name='userdata'),
    path('book-ticket/', views.bookticket, name='bookticket'),
    path('change-ticket/<str:pk>', views.changeticket, name='changeticket'),
    path('delete-ticket/<str:pk>', views.deleteticket, name='deleteticket'),
  
    path('login/', views.loginuser,name='login'),
    path('logout/', views.logoutuser,name='logout'),
    path('register/',views.registeruser,name='register'),
]
