from django.contrib import admin
#
from .models import Paciente
# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres',
        'apellidos',
        'tipo_documento',
        'nro_documento',
        'email',
        'genero',
        'fecha_nacimiento',
        'edad',
        'eps',
        'telefono',
    )


admin.site.register(Paciente, PacienteAdmin)