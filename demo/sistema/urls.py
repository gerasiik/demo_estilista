from django.contrib import admin
from django.urls import path
from .views import (
    UsuariosListado,
    UsuariosCrear,
    UsuarioActualizar,
    UsuarioEliminar,
    UsuarioDetalle,
)

urlpatterns = [
    # La ruta 'leer' en donde listamos todos los registros o usuarios de la Base de Datos
    path("", UsuariosListado.as_view(template_name="core/index.html"), name="leer"),
    path(
        "crear/",
        UsuariosCrear.as_view(template_name="core/crear.html"),
        name="crear",
    ),
    path(
        "actualizar/<int:pk>/",
        UsuarioActualizar.as_view(template_name="core/actualizar.html"),
        name="actualizar",
    ),
    path("eliminar/<int:pk>/", UsuarioEliminar.as_view(), name="eliminar"),
    path(
        "detalle/<int:pk>/",
        UsuarioDetalle.as_view(template_name="core/detalles.html"),
        name="detalle",
    ),
]
