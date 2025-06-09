from django.shortcuts import render, redirect, get_object_or_404
from .models import SistemaOperativo
from django.contrib import messages

# Create your views here.

# LISTADO DE SISTEMAS OPERATIVOS
def inicio(request):
    sistemas_operativos = SistemaOperativo.objects.all()
    return render(request, "inicio.html", {'sistemas_operativos': sistemas_operativos})

# FORMULARIO NUEVO SISTEMA OPERATIVO
def nuevoSO(request):
    return render(request, "nuevoSO.html")

# GUARDAR SISTEMA OPERATIVO
def guardarSO(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        version = request.POST["version"]

        SistemaOperativo.objects.create(
            nombre=nombre,
            version=version
        )

        messages.success(request, "Sistema Operativo guardado exitosamente")
        return redirect('/')
    return redirect('/')

# ELIMINAR SISTEMA OPERATIVO
def eliminarSO(request, id):
    soEliminar = get_object_or_404(SistemaOperativo, id=id)
    soEliminar.delete()
    messages.success(request, "Sistema Operativo eliminado exitosamente")
    return redirect('/')

# FORMULARIO DE EDICIÓN
def editarSO(request, id):
    soEditar = get_object_or_404(SistemaOperativo, id=id)
    return render(request, "editarSO.html", {'soEditar': soEditar})

# PROCESAR EDICIÓN
def procesarEdicionSO(request):
    if request.method == "POST":
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        version = request.POST["version"]

        try:
            so = SistemaOperativo.objects.get(id=id)
            so.nombre = nombre
            so.version = version
            so.save()
            messages.success(request, "Sistema Operativo actualizado exitosamente")
        except SistemaOperativo.DoesNotExist:
            messages.error(request, "Sistema Operativo no encontrado")

        return redirect('/')
    return redirect('/')
