from django.contrib import admin
#
from .models import Examen
# Register your models here.


class ExamenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_examen',
    )


admin.site.register(Examen, ExamenAdmin)