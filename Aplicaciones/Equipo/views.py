from django.shortcuts import render,redirect
from .models import SistemaOperativo
from .models import Equipo
from django.contrib import messages
# Create your views here.

def inicio(request):
    listadoEquipo=Equipo.objects.all()
    return render(request,"inicioeq.html",{'equipo':listadoEquipo})
def nuevoEquipo(request):
    rsistema_operatvo=SistemaOperativo.objects.all()
    return render(request,"nuevoEquipo.html",{'sistema_operativo':rsistema_operatvo})

def guardarEquipo(request):
    nombre = request.POST["nombre"]
    marca = request.POST["marca"]
    modelo = request.POST["modelo"]
    procesador = request.POST["procesador"]
    sistema_operativoid = request.POST["sistema_operativo"]
    sistema_operativo=SistemaOperativo.objects.get(id=sistema_operativoid)
     #Subiendo archivo
    fotoe=request.FILES.get("fotoe")
    #Archivo
    fichatec=request.FILES.get("fichatec")
    nuevoEquipo=Equipo.objects.create(
            nombre=nombre,
            marca=marca,
            modelo=modelo,
            procesador=procesador,
            fotoe=fotoe,
            fichatec=fichatec,
            sistema_operativo=sistema_operativo,
        )
    #mensaje de confirmacion
    messages.success(request,"Equipo guardado exitosamente")
    return redirect('inicioeq')

def eliminarEquipo(request,id):
    equipoEliminar = Equipo.objects.get(id=id)
    equipoEliminar.delete()
    messages.success(request,"Equipo ELIMINADO exitosamente")
    return redirect('inicioeq')

#editar
def editarEquipo(request,id):
    equipoEditar=Equipo.objects.get(id=id)
    rsistema_operativo=SistemaOperativo.objects.all()
    return render(request,"editarEquipo.html",{'equipoEditar':equipoEditar,'sistema_operativo':rsistema_operativo})

def procesarEdicionEquipo(request):
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    marca = request.POST["marca"]
    modelo = request.POST["modelo"]
    procesador = request.POST["procesador"]

      #Subiendo archivo
    fotoes=request.FILES.get("fotoe")
    #Archivo
    fichatecs=request.FILES.get("fichatec")

    sistema_operativoid = request.POST["sistema_operativo"]
    sistema_operativo=SistemaOperativo.objects.get(id=sistema_operativoid)
    equipo=Equipo.objects.get(id=id)
    equipo.nombre=nombre
    equipo.marca=marca
    equipo.modelo= modelo
    equipo.procesador= procesador

    if fotoes:
        equipo.fotoe= fotoes
    if fichatecs:
        equipo.fichatec=fichatecs

    equipo.save()
    #mensaje de confirmacion
    messages.success(request,"Equipo ACTUALIZADO exitosamente")
    return redirect('inicioeq')