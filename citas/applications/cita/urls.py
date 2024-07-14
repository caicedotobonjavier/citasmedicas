from django.urls import path, re_path, include
#
from . import views

app_name = 'cita_app'


urlpatterns = [
    path('asignar-cita/', views.AsignarCitaView.as_view(), name='asignar_cita'),
    path('todas_las_citas/', views.VerCitasAsignadaView.as_view(), name='todas_las_citas'),
    path('actualizar-cita/<pk>/', views.ModificarCitasView.as_view(), name='actualizar__citas'),
]
