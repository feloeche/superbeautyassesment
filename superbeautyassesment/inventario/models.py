"""Inventario models."""

#Django
from tkinter import E
from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    """Equipo Model."""

    referencia = models.CharField(max_length=20)
    marca = models.CharField(max_length=10)
    procesador = models.CharField(max_length=40)
    memoria = models.CharField(max_length=20)
    disco = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.referencia


class EquipoUsuario(models.Model):
    """EquipoUser Model"""

    usuario = models.ForeignKey(User, on_delete=models.CASCADE ) 
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, limit_choices_to={'enable':True})
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} asignado a {}'.format(self.equipo, self.usuario.username)

    def save(self, *args, **kwargs):
        device = self.equipo
        deactivate = Equipo.objects.get(referencia=device)
        deactivate.enable = False
        deactivate.save()
        super(EquipoUsuario, self).save(*args, **kwargs)
        import pdb; pdb.set_trace()

                
