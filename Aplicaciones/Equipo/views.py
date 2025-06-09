from django.shortcuts import render,redirect
from .models import SistemaOperativo
from .models import Equipo
from django.contrib import messages
# Create your views here.

def inicio(request):
    listadoEquipo=Equipo.objects.all()
    return render(request,"inicioeqtml",{'equipo':listadoEquipo})
def nuevoEquipo(request):
    rsistema_operatvo=SistemaOperativo.objects.all()
    return render(request,"nuevoMuestreo.html",{'sistema_operativo':rsistema_operatvo})

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