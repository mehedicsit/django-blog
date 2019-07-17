from django.contrib import admin
from django.urls import path
from .import views 
urlpatterns = [
    
    path('', views.blogindex , name="index"),
    path('about/', views.aboutUs , name="about"),
    path('post/<int:pk>/', views.singlePost, name='singlePost'),
]