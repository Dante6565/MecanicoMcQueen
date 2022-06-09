from django.db import models

class Contacto(models.Model):
    id_contacto = models.IntegerField(primary_key=True, verbose_name='ID Contacto')
    nombre_contacto = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=50, verbose_name='Email')
    mensaje = models.TextField(default="No ingreso mensaje", verbose_name="Mensaje")
    def __str__(self):
        return str(self.nombre_contacto)


