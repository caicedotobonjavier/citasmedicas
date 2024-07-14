from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.paciente.models import Paciente
#
from applications.eps.models import Eps
#
from .managers import CitaManager
# Create your models here.


class Cita(TimeStampedModel):
    fecha_actual = models.DateField('Cita dada el dia')
    fecha_cita = models.DateField('Cita para el dia')
    hora_cita = models.TimeField('Hora Cita')
    historia_clinica = models.CharField('Historia Clinica', max_length=20)
    paciente = models.ForeignKey(Paciente, related_name='cita_paciente', on_delete=models.CASCADE)
    eps = models.ForeignKey(Eps, related_name='cita_eps', on_delete=models.CASCADE)
    codigo_autorizacion = models.CharField('Codigo Autorizacion', max_length=20)
    tipo_estudio = models.CharField('Tipo de Estudio', max_length=20)
    obsernaciones = models.TextField('Observaciones', blank=True)

    objects = CitaManager()

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['fecha_cita', 'hora_cita']
        unique_together = ['fecha_cita', 'hora_cita']
    

    def __str__(self):
        return str(self.fecha_cita) + ' - ' + str(self.hora_cita) + ' - ' + str(self.paciente.nombres) + ' ' + str(self.paciente.apellidos)