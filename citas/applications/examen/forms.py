from django import forms
#
from .models import Examen


class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = (
            'nombre_examen',
        )

        widgets = {
            'nombre_examen' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre del nuevo examen'
                }
            ),
        }