#configuracion de rutas
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicioMe),
    path('nuevoMedicamento/',views.nuevoMedicamento),
    path('guardarMedicamento/',views.guardarMedicamento),
    path('eliminarMedicamento/<id>',views.eliminarMedicamento),
    path('editarMedicamentos/<id>',views.editarMedicamentos),
    path('procesarEdicionMedicamento/<id>',views.procesarEdicionMedicamento),
    ]