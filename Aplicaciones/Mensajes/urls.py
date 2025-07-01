from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicioMen),
    path('nuevoMensaje/',views.nuevoMensaje),
    path('guardarMensaje/',views.guardarMensaje),
    path('eliminarMensaje/<id>',views.eliminarMensaje),
    path('editarMensaje/<id>',views.editarMensaje),
    path('procesarEdicionMensaje/<id>',views.procesarEdicionMensaje),
    ]