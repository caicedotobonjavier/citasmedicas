from django.shortcuts import render
#
from .models import Examen
#
from django.views.generic import FormView
#
from .forms import ExamenForm
#
from django.urls import reverse_lazy
# Create your views here.

class ExamenView(FormView):
    template_name = 'examen/nuevo-examen.html'
    form_class = ExamenForm
    success_url = reverse_lazy('examen_app:agregar_examen')

    def form_valid(self, form):

        Examen.objects.create(
            nombre_examen = form.cleaned_data['nombre_examen']
        )

        return super(ExamenView, self).form_valid(form)