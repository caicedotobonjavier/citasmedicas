from django.db import models
#


class CitaManager(models.Manager):    

    def citas_del_paciente(self, dato):
        consulta = self.filter(
            paciente__id = dato
        ).order_by('created')

        return consulta
    

    def consultar_citas(self, cedula, fecha_1, fecha_2):
        if cedula:
            resultado = self.filter(
                paciente__nro_documento = cedula
            )
            return resultado
        elif fecha_1 and fecha_2:
            resultado = self.filter(
                fecha_cita__gte=fecha_1,
                fecha_cita__lte=fecha_2
            )
            return resultado
        else:
            return self.all()