from django.shortcuts import render,redirect
from .models import Medico
from django.contrib import messages
# Create your views here.
def inicioM(request):
    listadoMedicos=Medico.objects.all()
    return render(request,"inicioM.html",{'medicos':listadoMedicos})

#-----------------------------------------
def nuevoMedico(request):
    return render(request,"nuevoMedico.html")

#----------------------------------------------
def guardarMedico(request):
    nombre=request.POST["nombre"]
    especialidad=request.POST["especialidad"]
    consultorio=request.POST["consultorio"]
    horario=request.POST["horario"]
    licencia=request.POST["licencia"]
    contacto=request.POST["contacto"]
    nuevoMedico=Medico.objects.create(nombre=nombre,especialidad=especialidad,consultorio=consultorio,horario=horario,licencia=licencia,contacto=contacto)
    messages.success(request,"Cargo guardado exitosamente")
    return redirect('/medicos/')

#----------------------------------
def eliminarMedico(request,id):
    medicoEliminar=Medico.objects.get(id=id)
    medicoEliminar.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect('/medicos/')
# ---------------------------------------
def editarMedico(request,id):
    medicoEditar=Medico.objects.get(id=id)
    return render(request,"editarMedico.html",{'medicoEditar':medicoEditar})
#----------------------------------------
def procesarEdicionMedico(request, id):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    especialidad=request.POST["especialidad"]
    consultorio=request.POST["consultorio"]
    horario=request.POST["horario"]
    licencia=request.POST["licencia"]
    contacto=request.POST["contacto"]

    medico=Medico.objects.get(id=id)#buscar el cargo a editar por id
    medico.nombre=nombre
    medico.especialidad=especialidad
    medico.consultorio=consultorio
    medico.horario=horario
    medico.licencia=licencia
    medico.contacto=contacto
    medico.save()
    messages.success(request,"Cargo ACTUALIZADO exitosamente")
    return redirect('/medicos/')
