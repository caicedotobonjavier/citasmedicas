from django.contrib import admin
#
from .models import Eps
# Register your models here.

class EpsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )


admin.site.register(Eps, EpsAdmin)