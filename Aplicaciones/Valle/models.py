# Aplicaciones/Valle/models.py
from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario
