from django.db import models

# Create your models here.
class Curso (models.Model):

    nombre = models.CharField(max_length=40, null=True)
    camada = models.IntegerField(null=True)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)



