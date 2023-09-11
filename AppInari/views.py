from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Producto, Cliente, Carrito

def producto(req):
    return render(req, "producto.html")

def cliente(req):
    return render(req, "clientes.html")

def carrito(req):
    return render(req, "carrito.html")

