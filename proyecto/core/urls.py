from django import views
from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name="home"),
    path('contact', contacto, name="contacto"),
    path('about', about, name="about"),
    path('adminView.html', AdminView , name="AdminView"),
    path('adminViewConsultas.html', AdminViewConsultas , name="AdminViewConsultas"),
    path('registrarContacto/', registrarContacto),
]
