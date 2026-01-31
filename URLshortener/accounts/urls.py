from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('home/', views.homeView, name='home'),
    path('login/', views.loginView, name ='login'),
]