from django.shortcuts import render
#
from .models import Cita
#
from django.views.generic import FormView, TemplateView, UpdateView, ListView
#
from .forms import AsignarCitaForm, ActualizarCitaForm
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from django.core.mail import send_mail
#
from .functions import send_mail_google
# Create your views here.


class AsignarCitaView(FormView):
    template_name = 'cita/asignar-cita.html'
    form_class = AsignarCitaForm
    success_url = reverse_lazy('cita_app:todas_las_citas')


    def form_valid(self, form):

        cita_medica = Cita.objects.create(
            fecha_actual = form.cleaned_data['fecha_actual'],
            fecha_cita = form.cleaned_data['fecha_cita'],
            hora_cita = form.cleaned_data['hora_cita'],
            historia_clinica = form.cleaned_data['historia_clinica'],
            paciente = form.cleaned_data['paciente'],
            eps = form.cleaned_data['eps'],
            codigo_autorizacion = form.cleaned_data['codigo_autorizacion'],
            examen = form.cleaned_data['examen'],
            obsernaciones = form.cleaned_data['obsernaciones'],
        )

        #enviar codigo al email del usaurio con send_mail
        #asunto = 'Asignacion cita cardiologia'
        #mensaje = f"""Cordial Saludo,
        #\nConfirmacion de cita medica para el paciente {cita_medica.paciente}.
        #\nFecha cita: {cita_medica.fecha_cita}
        #\nHora cita: {cita_medica.hora_cita}
        #\nRecuerde presentarse 20 minutos antes, presentarse con el documento de identidad original y examenes previos si los tiene.
        #\nFeliz dia."""
#
        #email_remitente = 'jacto2024@gmail.com'
        ##
        #send_mail(asunto, mensaje, email_remitente, [cita_medica.paciente.email],)


        #OTRA FORMA DE ENVIAR CORREOS
        if cita_medica.paciente.email:
            send_mail_google(cita_medica.paciente.email, cita_medica.fecha_cita, cita_medica.hora_cita, cita_medica.paciente)
        

        return HttpResponseRedirect(
            reverse(
                'cita_app:todas_las_citas',
            )
        )


class VerCitasAsignadaView(ListView):
    template_name = 'cita/citas-asignadas.html'
    model = Cita
    context_object_name = 'citas'
    paginate_by = 6


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