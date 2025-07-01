#configuracion de rutas
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicioM),
    path('nuevoMedico/',views.nuevoMedico),
    path('guardarMedico/',views.guardarMedico),
    path('eliminarMedico/<id>',views.eliminarMedico),
    path('editarMedico/<id>',views.editarMedico),
    path('procesarEdicionMedico/<id>',views.procesarEdicionMedico),
    ]