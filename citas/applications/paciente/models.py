from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.eps.models import Eps
#
from .managers import PacienteManager
# Create your models here.

class Paciente(TimeStampedModel):

    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = '2'

    CHOICES_GENERO = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    )


    REGISTRO_CIVIL = '0'
    TARJETA_IDENTIDAD = '1'
    CEDULA_CIUDADANIA = '2'
    TARJETA_EXTRANJERIA = '3'
    OTRO = '4'

    CHOICES_TIPO_DOCUMENTO = (
        (REGISTRO_CIVIL, 'Registro Civil'),
        (TARJETA_IDENTIDAD, 'Tarjeta Identidad'),
        (CEDULA_CIUDADANIA, 'Cedula Ciudadania'),
        (TARJETA_EXTRANJERIA, 'Tarjeta Extranjeria'),
        (OTRO, 'Otro'),
    )


    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    tipo_documento = models.CharField('Tipo Documento', max_length=1, choices=CHOICES_TIPO_DOCUMENTO)
    nro_documento = models.CharField('N° Documento', max_length=20, unique=True)
    email = models.EmailField('Correo Electrnico', max_length=254, unique=True, blank=True, null=True)
    genero = models.CharField('Genero', max_length=1, choices=CHOICES_GENERO, blank=True)
    fecha_nacimiento = models.DateField('Fecha Nacimiento')
    edad = models.IntegerField('Edad', blank=True)
    eps = models.ForeignKey(Eps, related_name='paciente_eps', on_delete=models.CASCADE)
    telefono = models.CharField('Telefono Contacto', max_length=20, blank=True)

    objects = PacienteManager()


    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['nombres']
    

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

