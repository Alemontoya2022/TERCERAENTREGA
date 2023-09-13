from django.contrib import admin
from .models import Producto, Clientes, Carrito
from datetime import datetime

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio']
    search_fields = ['nombre', 'precio']
    list_filter = ['nombre']

    def antiguedad(self, object):
        print('**********',object)
        if object.fecha_creacion:
            return (datetime.now().date() - object.fecha_creacion).days

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Clientes)
admin.site.register(Carrito)

# Register your models here.
