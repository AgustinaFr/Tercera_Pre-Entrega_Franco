from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    mail = models.EmailField()

class Libros(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)

class Generos(models.Model):
    nombre_genero = models.CharField(max_length=40)

