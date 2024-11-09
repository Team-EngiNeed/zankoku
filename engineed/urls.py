from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('researchers',views.researchers, name='researchers'),
    path('login/', views.login, name='login'),
    path('students/', views.students, name='students'),  # Add URL for students page
]