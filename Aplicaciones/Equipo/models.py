from django.db import models
from Aplicaciones.SistemaOperativo.models import SistemaOperativo

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    fotoe = models.FileField(upload_to='equipos')
    fichatec = models.FileField(upload_to='equipos')
    sistema_operativo = models.ForeignKey(SistemaOperativo, on_delete=models.CASCADE)
