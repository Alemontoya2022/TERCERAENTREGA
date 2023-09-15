from django.urls import path
from .views import *
from AppInari import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('producto/', views.producto, name="Producto"),
    path('clientes/', views.clientes, name="Clientes"),
    path('carrito/', views.carrito , name="Carrito"),
    path('cliente-formulario/', clienteFormulario, name="clienteFormulario"),
    path('producto-formulario/', productoFormulario, name="productoFormulario"),
    path('lista-productos/', listar_producto, name='ListaProductos'),
    path('productosInari/', productosInari, name='productosInari'),
    path('busquedaProducto/', views.busquedaProducto, name='busquedaProducto'),
    path('buscar/', buscar, name="Buscar"),
    ]