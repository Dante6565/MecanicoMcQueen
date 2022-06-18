from django.shortcuts import render, redirect
from .models import Contacto
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def AdminView(request):
    return render(request, 'core/AdminView.html')

def AdminViewConsultas(request):
    contacto = Contacto.objects.all()
    return render(request, 'core/adminViewConsultas.html',{"contacto": contacto})


def registrarContacto(request):
    nombre = request.POST.get('txtNombre')
    email = request.POST.get('txtEmail')
    mensaje = request.POST.get('txtMensaje')
    Contacto.objects.create(id_contacto= 31, nombre_contacto = nombre, email=email, mensaje=mensaje)
    messages.success(request, '¡Contacto enviado registrado!')
    return redirect('/')
