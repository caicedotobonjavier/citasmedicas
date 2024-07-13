from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.

class Eps(TimeStampedModel):
    nombre = models.CharField('Eps', max_length=50)

    class Meta:
        verbose_name = 'EPS'
        verbose_name_plural = 'EPS'
        ordering = ['nombre']
    

    def __str__(self):
        return self.nombre
