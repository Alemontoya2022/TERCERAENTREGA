from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Producto

def producto(self):
    producto = Producto(nombre="Shampoo Solido", precio="2000")
    producto.save()
    documentoDeTexto = f"--->Producto: {producto.nombre} Precio: {producto.precio}"

    return HttpResponse(documentoDeTexto)
