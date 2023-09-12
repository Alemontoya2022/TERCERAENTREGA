"""
<<<<<<< HEAD
URL configuration for ProyectoCoder project.
=======
URL configuration for INARI project.
>>>>>>> a28d1498d5875a7b9648b4d0659bad062d430a1a

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from AppInari.views import Clientes, listar_clientes

=======
>>>>>>> a28d1498d5875a7b9648b4d0659bad062d430a1a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppInari/', include('AppInari.urls')),
]
