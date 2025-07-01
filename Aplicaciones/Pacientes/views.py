from django.shortcuts import render,redirect
#importar paciente
from .models import Paciente
from django.contrib import messages
# Create your views here.
#funcion para renderizar el listado de pacientes
def inicioP(request):
    listadoPacientes=Paciente.objects.all()
    return render(request,"inicioP.html",{'pacientes':listadoPacientes})

#funcion renderisando fomrulario de nuevo paciente
def nuevoPaciente(request):
    return render(request,"nuevoPaciente.html")

#almacenando de bdd
def guardarPaciente(request):
    nombre=request.POST["nombre"]
    cedula=request.POST["cedula"]
    edad=request.POST["edad"]
    tipo_sangre=request.POST["tipo_sangre"]
    seguro=request.POST["seguro"]
    direccion=request.POST["direccion"]
    nuevoPaciente=Paciente.objects.create(nombre=nombre,cedula=cedula,edad=edad,tipo_sangre=tipo_sangre,seguro=seguro,direccion=direccion)
    messages.success(request,"Cargo guardado exitosamente")
    return redirect('/')

#eliminar por ID
def eliminarPaciente(request,id):
    pacienteEliminar=Paciente.objects.get(id=id)
    pacienteEliminar.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect('/')

def editarPaciente(request,id):
    pacienteEditar=Paciente.objects.get(id=id)
    return render(request,"editarPaciente.html",{'pacienteEditar':pacienteEditar})

def procesarEdicionPaciente(request, id):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    cedula=request.POST["cedula"]
    edad=request.POST["edad"]
    tipo_sangre=request.POST["tipo_sangre"]
    seguro=request.POST["seguro"]
    direccion=request.POST["direccion"]

    paciente=Paciente.objects.get(id=id)#buscar el cargo a editar por id
    paciente.nombre=nombre
    paciente.cedula=cedula
    paciente.edad=edad
    paciente.tipo_sangre=tipo_sangre
    paciente.seguro=seguro
    paciente.direccion=direccion
    paciente.save()
    messages.success(request,"Cargo ACTUALIZADO exitosamente")
    return redirect('/')