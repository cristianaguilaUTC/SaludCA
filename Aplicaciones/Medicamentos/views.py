from django.shortcuts import render,redirect
#importar el medicamento
from .models import Medicamento
#importar componentes para mensages
from django.contrib import messages


# Create your views here.
#funcion para renderizar el listado
def inicioMe(request):
    listadoMedicamentos=Medicamento.objects.all()
    return render(request,"inicioMe.html",{'medicamentos':listadoMedicamentos})

#funcion renderizado formulario
def nuevoMedicamento(request):
    return render(request,"nuevoMedicamento.html")

#almacenando de bdd
def guardarMedicamento(request):
    nombre=request.POST["nombre"]
    laboratorio=request.POST["laboratorio"]
    dosis=request.POST["dosis"]
    presentacion=request.POST["presentacion"]
    precio=request.POST["precio"]
    caducidad=request.POST["caducidad"]
    nuevoMedicamento=Medicamento.objects.create(nombre=nombre,laboratorio=laboratorio,dosis=dosis,presentacion=presentacion,precio=precio,caducidad=caducidad)
    messages.success(request,"medicamento guardado exitosamente")
    return redirect('/medicamentos/')

#eliminar por ID
def eliminarMedicamento(request,id):
    medicamentoEliminar=Medicamento.objects.get(id=id)
    medicamentoEliminar.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect('/medicamentos/')
#mostrando el formulario
def editarMedicamentos(request,id):
    medicamentosEditar=Medicamento.objects.get(id=id)
    return render(request,"editarMedicamentos.html",{'medicamentosEditar':medicamentosEditar})
#actualizando cargos de la dbb
def procesarEdicionMedicamento(request, id):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    laboratorio=request.POST["laboratorio"]
    dosis=request.POST["dosis"]
    presentacion=request.POST["presentacion"]
    precio=request.POST["precio"]
    caducidad=request.POST["caducidad"]

    medicamento=Medicamento.objects.get(id=id)#buscar el cargo a editar por id
    medicamento.nombre=nombre
    medicamento.laboratorio=laboratorio
    medicamento.dosis=dosis
    medicamento.presentacion=presentacion
    medicamento.precio=precio
    medicamento.caducidad=caducidad
    medicamento.save()
    messages.success(request,"Cargo ACTUALIZADO exitosamente")
    return redirect('/medicamentos/')