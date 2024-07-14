from django import forms
#
from .models import Eps


class EpsForm(forms.ModelForm):
    class Meta:
        model = Eps
        fields = (
            'nombre',
        )

        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre de la EPS'
                }
            )
        }