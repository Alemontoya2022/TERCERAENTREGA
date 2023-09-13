from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Producto, Clientes, Carrito
from .forms import ClienteFormulario, ProductoFormulario

def inicio(req):

    return render(req, "inicio.html")

def producto(req, nombre, precio):

    producto = Producto(nombre=nombre, precio=precio)
    producto.save()

    return HttpResponse(f"""
    <p>Producto: {producto.nombre} - Precio: {producto.precio} creado con éxito!</p>
    """)

def listar_producto(req):

    lista = Producto.objects.all()

    return render(req, "lista_producto.html", {"lista_producto": lista})




def clientes(req, nombre, apellido):

    clientes = Clientes(nombre=nombre, apellido=apellido)
    clientes.save()

    return HttpResponse(f"""
    <p>Curso: {clientes.nombre} - Apellido: {clientes.apellido} creado con éxito!</p>
    """)


def carrito(req):
    
    return render(req, "carrito.html")

def listar_clientes(req):
    lista = Clientes.objects.all()
    return render(req, "lista_clientes.html", {"lista_clientes": lista})

def clienteFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = clienteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            cliente = Clientes(nombre=data["cliente"], apellido=data["apellido"])
            cliente.save()

            return render(req, "inicio.html")
    else:

        miFormulario = ClienteFormulario()
        return render(req, "clienteFormulario.html", {"miFormulario": miFormulario})
    
def productoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = productoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            producto = Producto(nombre=data["producto"], precio=data["precio"])
            producto.save()

            return render(req, "inicio.html")
    else:

        miFormulario = ClienteFormulario()
        return render(req, "productoFormulario.html", {"miFormulario": miFormulario})
