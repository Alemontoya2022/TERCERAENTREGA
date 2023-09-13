from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('producto/', producto, name="Producto"),
    path('clientes/', clientes, name="Clientes"),
    path('carrito/', carrito , name="Carrito"),
    path('cliente-formulario/', clienteFormulario, name="clienteFormulario"),
    path('producto-formulario/', productoFormulario, name="productoFormulario"),
    path('lista-productos/', listar_producto, name='ListaProductos'),
    ]