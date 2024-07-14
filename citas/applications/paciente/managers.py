from django.db import models
#
from django.db.models import Q


class PacienteManager(models.Manager):

    def buscar_paciente(self, dato):
        if dato:
            consulta = self.filter(
                Q(nombres__icontains=dato) | Q(nro_documento__icontains=dato)
            )
            return consulta
        else:
            return self.all()
    

    def consultar_paciente(self, dato):
        consulta = self.filter(
            id = dato
        )
        return consulta
    

    