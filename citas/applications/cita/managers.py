from django.db import models
#


class CitaManager(models.Manager):
    

    def citas_del_paciente(self, dato):
        consulta = self.filter(
            paciente__id = dato
        ).order_by('created')

        return consulta