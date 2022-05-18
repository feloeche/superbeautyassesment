"""Inventario admin clases"""

#Django
from tkinter import E
from django.contrib import admin

# Models
from inventario.models import Equipo, EquipoUsuario

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    """Equipo admin"""

    list_display = ('id', 'referencia', 'marca', 'tipo')
    list_display_links = ('id', 'referencia')
    list_filter = ('tipo',)
    search_fields = ('referencia',)

    


@admin.register(EquipoUsuario)
class EquipoUsuarioAdmin(admin.ModelAdmin):
    """Equipo Usuario Admin."""

    list_display = ('id', 'equipo', 'usuario', 'fecha_asignacion')
    list_display_links = ('id', 'equipo')
    list_filter = ('fecha_asignacion','usuario')


    def enable_device(self, obj):
        device = obj.equipo
        device.enable = False
        device.save(update_fields=['enable'])

            
    
        

    