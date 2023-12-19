from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Usuarios

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms


class UsuariosListado(ListView):
    model = (
        Usuarios  # Llamamos a la clase 'Usuarios' que se encuentra en nuestro archivo
    )


class UsuariosCrear(SuccessMessageMixin, CreateView):
    model = Usuarios  # Llamamos a la clase 'Usuaurios' que se encuentra en nuestro archivo 'mode
    form = Usuarios  # Definimos nuestro formulario con el nombre de la clase o modelo 'Usuarios
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'sistema' de nuestra Base de Datos
    success_message = "Usuario Creado Correctamente !"  # Mostramos este Mensaje luego de Crear un Usuario

    # Redireccionamos a la página principal luego de crear un registro o usuario
    def get_success_url(self):
        return reverse("leer")  # Redireccionamos a la vista principal 'leer'


class UsuarioDetalle(DetailView):
    model = Usuarios  # Llamamos a la clase 'Usuarios' que se encuentra en nuestro archivo 'models.py'


class UsuarioActualizar(SuccessMessageMixin, UpdateView):
    model = Usuarios  # Llamamos a la clase 'Usuarios' que se encuentra en nuestro archivo 'models.py'
    form = Usuarios  # Definimos nuestro formulario con el nombre de la clase o modelo 'Usuarios'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Usuarios' de nuestra Base de Datos
    success_message = "Usuario Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un usuario

    # Redireccionamos a la página principal luego de actualizar un registro o usuario
    def get_success_url(self):
        return reverse("leer")  # Redireccionamos a la vista principal 'leer'


class UsuarioEliminar(SuccessMessageMixin, DeleteView):
    model = Usuarios
    form = Usuarios
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o usuario
    def get_success_url(self):
        success_message = "Usuario Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Usuario
        messages.success(self.request, (success_message))
        return reverse("leer")  # Redireccionamos a la vista principal 'leer'
