from django import forms
#
from .models import Paciente


class AgregarPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = (
            'nombres',
            'apellidos',
            'tipo_documento',
            'nro_documento',
            'email',
            'genero',
            'fecha_nacimiento',
            'edad',
            'eps',
            'telefono',
        )

        widgets = {
            'nombres' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre del paciente'
                }
            ),

            'apellidos' : forms.TextInput(
                attrs={
                    'placeholder' : 'Apellidos del paciente'
                }
            ),

            'nro_documento' : forms.TextInput(
                attrs={
                    'placeholder' : 'Numero del documento'
                }
            ),

            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo electronico'
                }
            ),

            'fecha_nacimiento' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            ),

            'edad' : forms.NumberInput(
                attrs={
                    'placeholder' : 'Edad del paciente'
                }
            ),

            'telefono' : forms.TextInput(
                attrs={
                    'placeholder' : 'Telefono de contacto'
                }
            ),
        }