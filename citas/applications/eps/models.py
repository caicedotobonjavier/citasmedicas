from django.db import models
#
from model_utils.models import TimeStampedModel
#
from .managers import EpsManagers
# Create your models here.

class Eps(TimeStampedModel):
    nombre = models.CharField('Eps', max_length=50)

    objects = EpsManagers()

    class Meta:
        verbose_name = 'EPS'
        verbose_name_plural = 'EPS'
        ordering = ['id']
    

    def __str__(self):
        return self.nombre
