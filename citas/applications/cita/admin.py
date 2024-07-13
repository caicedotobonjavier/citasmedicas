from django.contrib import admin
#
from .models import Cita
# Register your models here.


class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_actual',
        'fecha_cita',
        'hora_cita',
        'historia_clinica',
        'paciente',
        'eps',
        'codigo_autorizacion',
        'tipo_estudio',
        'obsernaciones',
    )


admin.site.register(Cita, CitaAdmin)