from django.shortcuts import render
#
from django.views.generic import FormView, CreateView, UpdateView, ListView
#
from .models import Paciente
#
from .forms import AgregarPacienteForm
#
from django.urls import reverse_lazy
# Create your views here.


class AgregarPacienteView(FormView):
    template_name = 'paciente/agregar-paciente.html'
    form_class = AgregarPacienteForm
    success_url = reverse_lazy('paciente_app:agregar_paciente')

    def form_valid(self, form):        

        paciente = Paciente.objects.create(
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            tipo_documento = form.cleaned_data['tipo_documento'],
            nro_documento = form.cleaned_data['nro_documento'],
            email = form.cleaned_data['email'],
            genero = form.cleaned_data['genero'],
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
            edad = form.cleaned_data['edad'],
            eps = form.cleaned_data['eps'],
            telefono = form.cleaned_data['telefono']
        )

        return super(AgregarPacienteView, self).form_valid(form)