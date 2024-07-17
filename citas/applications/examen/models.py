from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.

class Examen(TimeStampedModel):
    nombre_examen = models.CharField('Nomde del Examen', max_length=100, unique=True)


    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'
        ordering = ['nombre_examen']
    

    def __str__(self):
        return self.nombre_examen
