from django import views
from django.urls import path
from .views import home, AdminView, AdminViewConsultas, registrarContacto

urlpatterns=[
    path('', home, name="home"),
    path('adminView.html', AdminView , name="AdminView"),
    path('adminViewConsultas.html', AdminViewConsultas , name="AdminViewConsultas"),
    path('registrarContacto/', registrarContacto),
]
