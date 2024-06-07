from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name ='home'),
    path('books/',book,name ='books'),
    path('customer/<str:pk>',customer,name='customer' ),
    path('create/',create,name='create'),
]
