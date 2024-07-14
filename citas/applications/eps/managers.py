from django.db import models


class EpsManagers(models.Manager):

    def consulta_eps(self, dato):
        if dato:
            resultado = self.filter(
                nombre__icontains = dato
            )
            return resultado
        else:
            return self.all()