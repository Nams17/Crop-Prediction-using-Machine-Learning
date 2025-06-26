from django.contrib import admin
from django.urls import path, include
from . import views
#ToDo
urlpatterns = [
    path('result/', views.cropResult, name = 'result'),
    path('', views.home)
]
