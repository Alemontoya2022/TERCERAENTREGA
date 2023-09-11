from django.urls import path
from AppInari import views

urlpatterns = [
    path('producto/', views.producto),
    path('cliente/', views.cliente),
    path('carrito/', views.carrito),
    ]