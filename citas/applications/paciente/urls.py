from django.urls import path, re_path, include
#
from . import views

app_name = 'paciente_app'


urlpatterns = [
    path('agregar-paciente/', views.AgregarPacienteView.as_view(), name='agregar_paciente'),
]
