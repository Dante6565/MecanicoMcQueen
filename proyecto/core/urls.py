from django import views
from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name="home"),
    path('contact', contacto, name="contacto"),
    path('about', about, name="about"),
    path('carrito', carrito, name="carrito"),
    path('adminview', AdminView , name="AdminView"),
    path('adminViewConsultas', AdminViewConsultas , name="AdminViewConsultas"),
    path('registrarContacto/', registrarContacto),
]
