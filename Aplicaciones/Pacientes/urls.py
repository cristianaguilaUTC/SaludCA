#configuracion de rutas
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicioP),
    path('nuevoPaciente/',views.nuevoPaciente),
    path('guardarPaciente/',views.guardarPaciente),
    path('eliminarPaciente/<id>',views.eliminarPaciente),
    path('editarPaciente/<id>',views.editarPaciente),
    path('procesarEdicionPaciente/<id>',views.procesarEdicionPaciente),
    ]