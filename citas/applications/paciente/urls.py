from django.urls import path, re_path, include
#
from . import views

app_name = 'paciente_app'


urlpatterns = [
    path('agregar-paciente/', views.AgregarPacienteView.as_view(), name='agregar_paciente'),
    path('todos-los-paciente/', views.ListaPacientesView.as_view(), name='todos_los_pacientes'),
    path('info-paciente/<pk>/', views.InformacionPaciente.as_view(), name='infos_pacientes'),
]
