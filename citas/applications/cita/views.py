from django.shortcuts import render
#
from .models import Cita
#
from django.views.generic import FormView, TemplateView, UpdateView, ListView
#
from .forms import AsignarCitaForm, ActualizarCitaForm
#
from django.urls import reverse_lazy
# Create your views here.


class AsignarCitaView(FormView):
    template_name = 'cita/asignar-cita.html'
    form_class = AsignarCitaForm
    success_url = reverse_lazy('cita_app:todas_las_citas')


    def form_valid(self, form):

        Cita.objects.create(
            fecha_actual = form.cleaned_data['fecha_actual'],
            fecha_cita = form.cleaned_data['fecha_cita'],
            hora_cita = form.cleaned_data['hora_cita'],
            historia_clinica = form.cleaned_data['historia_clinica'],
            paciente = form.cleaned_data['paciente'],
            eps = form.cleaned_data['eps'],
            codigo_autorizacion = form.cleaned_data['codigo_autorizacion'],
            tipo_estudio = form.cleaned_data['tipo_estudio'],
            obsernaciones = form.cleaned_data['obsernaciones'],
        )

        return super(AsignarCitaView, self).form_valid(form)


class VerCitasAsignadaView(ListView):
    template_name = 'cita/citas-asignadas.html'
    model = Cita
    context_object_name = 'citas'


    def get_queryset(self):
        cedula = self.request.GET.get('paciente')
        fecha_ini = self.request.GET.get('fecha1')
        fecha_fin = self.request.GET.get('fecha2')

        resultado = Cita.objects.consultar_citas(cedula, fecha_ini, fecha_fin)

        return resultado


class ModificarCitasView(UpdateView):
    template_name = 'cita/actualizar-cita.html'
    form_class = ActualizarCitaForm
    model = Cita
    success_url = reverse_lazy('cita_app:todas_las_citas')