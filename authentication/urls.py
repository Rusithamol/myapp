from django.urls import path
from .views import *  
urlpatterns = [
    path('',loginpage, name='loginpage'), 
    path('logout/',logoutUser, name='logout'),
    path('signup/',signupPage , name='signupPage'),
    path('home/',home ),
    path('adminpage/',adminpage)  
  
]

