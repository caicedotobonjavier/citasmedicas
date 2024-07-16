from django import forms
#
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email del usuario'
            }
        )
    )


    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña del usuario'
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Usuario o contraseña erroneo')
        

        return self.cleaned_data