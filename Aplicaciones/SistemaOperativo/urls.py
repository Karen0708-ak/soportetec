# Configuración de rutas específicas para la app Sistemas Operativos
from django.urls import path
from . import views

urlpatterns = [
    path('listarSO',views.inicio,name='listarSO'),
    path('nuevoSO', views.nuevoSO),
    path('guardarSO', views.guardarSO),
    path('eliminarSO/<id>', views.eliminarSO),
    path('editarSO/<id>', views.editarSO),
    path('procesarEdicionSO', views.procesarEdicionSO),
]
