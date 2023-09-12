from django.db import models

<<<<<<< HEAD
class Clientes(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        cel = models.IntegerField()
        email = models.EmailField(max_length=40)

        def __str__(self):
                return f'{self.nombre} {self.apellido}'
=======
class Cliente(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        cel = models.IntegerField()
        direccion = models.CharField(max_length=40)
>>>>>>> a28d1498d5875a7b9648b4d0659bad062d430a1a

class Producto(models.Model):
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()

<<<<<<< HEAD
        def __str__(self):
                return f'{self.nombre} {self.apellido}'

=======
>>>>>>> a28d1498d5875a7b9648b4d0659bad062d430a1a
class Carrito(models.Model):
        producto = models.CharField(max_length=40)
        pedido = models.CharField(max_length=40)
        total = models.IntegerField()
        

