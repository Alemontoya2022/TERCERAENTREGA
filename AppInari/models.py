from django.db import models

class Cliente(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        cel = models.IntegerField()
        direccion = models.CharField(max_length=40)

class Producto(models.Model):
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()

class Carrito(models.Model):
        producto = models.CharField(max_length=40)
        pedido = models.CharField(max_length=40)
        total = models.IntegerField()
        

