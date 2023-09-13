from django.db import models

class Clientes(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        cel = models.IntegerField()
        email = models.EmailField(max_length=40)

        def __str__(self):
                return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()

        def __str__(self):
                return f'{self.nombre} {self.precio}'

class Carrito(models.Model):
        producto = models.CharField(max_length=40)
        pedido = models.CharField(max_length=40)
        total = models.IntegerField()
        

