from django.shortcuts import render
#
from .models import Eps
#
from django.views.generic import ListView, FormView
#
from .forms import EpsForm
#
from django.urls import reverse_lazy
# Create your views here.

class AgregarEpsView(FormView):
    template_name = 'eps/agregar-eps.html'
    form_class = EpsForm
    success_url = reverse_lazy('eps_app:lista_eps')


    def form_valid(self, form):

        Eps.objects.create(
            nombre = form.cleaned_data['nombre']
        )

        return super(AgregarEpsView, self).form_valid(form)



class ListaEpsView(ListView):
    template_name = 'eps/lista-eps.html'
    context_object_name = 'eps'

    def get_queryset(self):
        dato = self.request.GET.get('eps')
        resultado = Eps.objects.consulta_eps(dato)

        return resultado
