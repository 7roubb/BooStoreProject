from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name ='home'),
    path('books/',book,name ='books'),
    path('customer/<str:pk>',customer,name='customer' ),
    path('create/',create,name='create'),
    path('update/<str:pk>',update,name='update'),
    path('delete/<str:pk>',delete_order,name='delete'),
    path('delete_book/<str:pk>',delete_book,name='deletebook')
  
]
