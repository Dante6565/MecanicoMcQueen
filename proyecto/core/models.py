from django.db import models

class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True, verbose_name='ID Contacto')
    nombreContacto = models.CharField(max_length=50, verbose_name='Nombre')
    emailContacto = models.EmailField(max_length=50, verbose_name='Email')
    mensajeContacto = models.TextField(default="No ingreso mensaje", verbose_name="Mensaje")
    
    def __str__(self):
        return self.idContacto




