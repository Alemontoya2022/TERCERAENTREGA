from django.urls import path
<<<<<<< HEAD
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('producto/', producto, name="Producto"),
    path('clientes/', clientes, name="Clientes"),
    path('carrito/', carrito , name="Carrito"),
=======
from AppInari import views

urlpatterns = [
    path('producto/', views.producto),
    path('cliente/', views.cliente),
    path('carrito/', views.carrito),
>>>>>>> a28d1498d5875a7b9648b4d0659bad062d430a1a
    ]