from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name='Id de Usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del usuario')
    apellido = models.CharField(max_length=50, verbose_name='Apellido del usuario')
    correo = models.CharField(max_length=100, verbose_name='Correo del usuario')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña del usuario')
    genero = models.CharField(max_length=5, verbose_name='Genero del usuario')

    def __str__(self):
        return self.correo


class Contacto(models.Model):
    idContacto = models.IntegerField(primary_key=True, verbose_name='Id de contacto')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario en el contacto')
    correo_usuario = models.CharField(max_length=100, verbose_name='Correo de Usuario en el contacto')
    mensaje_usuario = models.CharField(max_length=1000, verbose_name='Mensaje en el contacto')

    def __str__(self):
        return self.correo_usuario