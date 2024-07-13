from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    ADMINISTRADOR = '0'
    ENFERMERA = '1'
    DOCTOR = '2'
    ESPECIALISTA = '3'

    CHOICES_CARGO = (
        (ADMINISTRADOR, 'Administrador'),
        (ENFERMERA, 'Enfermera'),
        (DOCTOR, 'Doctor'),
        (ESPECIALISTA, 'Especialista'),
    )


    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = '2'

    CHOICES_GENERO = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro')
    )

    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre completo', max_length=50)
    cedula = models.CharField('N° Cedula', max_length=50, blank=True)
    genero = models.CharField('Genero', max_length=1, choices=CHOICES_GENERO, blank=True)
    cargo = models.CharField('Cargo', max_length=1, choices=CHOICES_CARGO, blank=True)
    telefono = models.CharField('Telefono contacto', max_length=10, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]


    def get_email(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name

