from django.shortcuts import *
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def AdminView(request):
    return render(request, 'core/AdminView.html')

def AdminViewConsultas(request):
    contacto = Contacto.objects.all()
    return render(request, 'core/adminViewConsultas.html',{"contacto": contacto})

def registrarContacto(request):

    data = request.POST
    nombreContacto=data['txtNombre']
    emailContacto=data['txtEmail']
    mensajeContacto=data['txtMensaje']

    contacto = Contacto.objects.create(
        nombreContacto=nombreContacto,
        emailContacto=emailContacto,
        mensajeContacto=mensajeContacto,
    )
    return redirect('/adminViewConsultas')
