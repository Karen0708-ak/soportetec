from django.shortcuts import render, redirect, get_object_or_404
from .models import SistemaOperativo
from django.contrib import messages

# LISTAR
def inicio(request):
    sistemas_operativos = SistemaOperativo.objects.all()
    return render(request, "listarSO.html", {'sistemas_operativos': sistemas_operativos})

# FORM NUEVO
def nuevoSO(request):
    return render(request, "nuevoSO.html")

# GUARDAR
def guardarSO(request):
    nombre = request.POST["nombre"]
    version = request.POST["version"]
    documentacion = request.FILES.get("documentacion")

    SistemaOperativo.objects.create(
        nombre=nombre,
        version=version,
        documentacion=documentacion
    )

    messages.success(request, "Sistema Operativo guardado exitosamente")
    return redirect('listarSO')

# FORM EDITAR
def editarSO(request, id):
    soEditar = get_object_or_404(SistemaOperativo, id=id)
    return render(request, "editarSO.html", {'soEditar': soEditar})

# PROCESAR EDICIÓN
def procesarEdicionSO(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    version = request.POST["version"]
    documentacion = request.FILES.get("documentacion")

    so = SistemaOperativo.objects.get(id=id)
    so.nombre = nombre
    so.version = version

    if documentacion:
        so.documentacion = documentacion 

    so.save()

    messages.success(request, "Sistema Operativo actualizado exitosamente")
    return redirect('listarSO')

# ELIMINAR
def eliminarSO(request, id):
    soEliminar = get_object_or_404(SistemaOperativo, id=id)
    soEliminar.delete()

    messages.success(request, "Sistema Operativo eliminado exitosamente")
    return redirect('listarSO')
