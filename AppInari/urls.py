from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('producto/', producto, name="Producto"),
    path('clientes/', clientes, name="Clientes"),
    path('carrito/', carrito , name="Carrito"),
    ]