from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Producto, Clientes, Carrito
from .forms import ClienteFormulario

def inicio(req):

    return render(req, "inicio.html")

def producto(req):

    return render(req, "producto.html")

def clientes(req):

    return render(req, "Clientes.html")


def carrito(req):
    
    return render(req, "carrito.html")

def listar_clientes(req):
    lista = Clientes.objects.all()
    return render(req, "lista_clientes.html", {"lista_clientes": lista})

def clienteFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            cliente = cliente(nombre=data["cliente"], apellido=data["apellido"])
            cliente.save()

            return render(req, "inicio.html")
    else:

        miFormulario = clienteFormulario()
        return render(req, "clienteFormulario.html", {"miFormulario": miFormulario})