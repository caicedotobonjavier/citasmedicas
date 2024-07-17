from django import forms
#
from .models import Cita


class AsignarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = (
            'fecha_actual',
            'fecha_cita',
            'hora_cita',
            'historia_clinica',
            'paciente',
            'eps',
            'codigo_autorizacion',
            'examen',
            'obsernaciones',
        )

        widgets = {
            'fecha_actual' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            ),

            'fecha_cita' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            ),

            'hora_cita' : forms.TimeInput(
                attrs={
                    'type' : 'time'
                }
            ),

            'historia_clinica' : forms.TextInput(
                attrs={
                    'placeholder' : 'Historia clinica'
                }
            ),

            'codigo_autorizacion' : forms.TextInput(
                attrs={
                    'placeholder' : 'Codigo de Autorizacion'
                }
            ),

            

            'obsernaciones' : forms.Textarea(
                attrs={
                    'placeholder' : 'Ingrese las observaciones',
                    'rows': '4'
                }
            ),
        }



class ActualizarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = (
            'fecha_actual',
            'fecha_cita',
            'hora_cita',
            'historia_clinica',
            'paciente',
            'eps',
            'codigo_autorizacion',
            'examen',
            'obsernaciones',
        )

        widgets = {
            'fecha_actual' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    
                    'type' : 'date'
                }
            ),

            'fecha_cita' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type' : 'date'
                }
            ),

            

            'hora_cita' : forms.TimeInput(
                attrs={
                    'type' : 'time'
                }
            ),

            'historia_clinica' : forms.TextInput(
                attrs={
                    'placeholder' : 'Historia clinica'
                }
            ),

            'codigo_autorizacion' : forms.TextInput(
                attrs={
                    'placeholder' : 'Codigo de Autorizacion'
                }
            ),

            'obsernaciones' : forms.Textarea(
                attrs={
                    'placeholder' : 'Ingrese las observaciones',
                    'rows': '4'
                }
            ),
        }