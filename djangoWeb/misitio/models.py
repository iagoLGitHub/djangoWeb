from django.db import models

# Create your models here.


class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fecha_alta = models.DateTimeField("Fecha de alta", blank=False, null=False)
    direccion = models.CharField(max_length=150, blank= False, null=True)
    mobile = models.CharField(max_length=150, blank=False, null=True)


