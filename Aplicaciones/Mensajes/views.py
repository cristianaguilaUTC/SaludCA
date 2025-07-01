from django.shortcuts import render,redirect
from .models import Mensaje
from django.contrib import messages
# Create your views here.
def inicioMen(request):
    listadoMensajes=Mensaje.objects.all()
    return render(request,"inicioMen.html",{'mensajes':listadoMensajes})

#-----------------------------------------
def nuevoMensaje(request):
    return render(request,"nuevoMensaje.html")

#----------------------------------------------
def guardarMensaje(request):
    remitente=request.POST["remitente"]
    destinatario=request.POST["destinatario"]
    contenido=request.POST["contenido"]
    fecha=request.POST["fecha"]
    asunto=request.POST["asunto"]
    nuevoMedico=Mensaje.objects.create(remitente=remitente,destinatario=destinatario,contenido=contenido,fecha=fecha,asunto=asunto)
    messages.success(request,"Cargo guardado exitosamente")
    return redirect('/mensajes/')

#----------------------------------
def eliminarMensaje(request,id):
    medicoEliminar=Mensaje.objects.get(id=id)
    medicoEliminar.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect('/mensajes/')
# ---------------------------------------
def editarMensaje(request,id):
    mensajeEditar=Mensaje.objects.get(id=id)
    return render(request,"editarMensaje.html",{'mensajeEditar':mensajeEditar})
#----------------------------------------
def procesarEdicionMensaje(request, id):
    id=request.POST["id"]
    remitente=request.POST["remitente"]
    destinatario=request.POST["destinatario"]
    contenido=request.POST["contenido"]
    fecha=request.POST["fecha"]
    asunto=request.POST["asunto"]

    medico=Mensaje.objects.get(id=id)#buscar el cargo a editar por id
    medico.remitente=remitente
    medico.destinatario=destinatario
    medico.contenido=contenido
    medico.fecha=fecha
    medico.asunto=asunto
    medico.save()
    messages.success(request,"Cargo ACTUALIZADO exitosamente")
    return redirect('/mensajes/')