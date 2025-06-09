# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('inicioeq',views.inicio,name='inicioeq'),
    path('nuevoEquipo',views.nuevoEquipo),
    path('guardarEquipo',views.guardarEquipo),
    
]