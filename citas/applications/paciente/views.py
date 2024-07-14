from django.db.models.query import QuerySet
from django.shortcuts import render
#
from django.views.generic import FormView, CreateView, UpdateView, ListView, DetailView
#
from .models import Paciente
#
from applications.cita.models import Cita
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



class ListaPacientesView(ListView):
    template_name = 'paciente/todos-los-pacientes.html'
    model = Paciente
    context_object_name = 'pacientes'

    def get_queryset(self):
        dato = self.request.GET.get('paciente')

        resultado = Paciente.objects.buscar_paciente(dato)

        return resultado



class InformacionPaciente(DetailView):
    template_name = 'paciente/informacion-paciente.html'
    context_object_name = "paciente"

    def get_queryset(self):
        dato = self.kwargs['pk']
        resultado =  Paciente.objects.consultar_paciente(dato)
        return resultado
    

    def get_context_data(self, **kwargs):
        context = super(InformacionPaciente, self).get_context_data(**kwargs)
        dato = self.kwargs['pk']
        context["historia_citas"] = Cita.objects.citas_del_paciente(dato)
        return context
    
    

    