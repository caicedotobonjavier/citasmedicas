from django.urls import path, re_path, include
#
from . import views

app_name = 'examen_app'


urlpatterns = [
    path('agregar-examen/', views.ExamenView.as_view(), name='agregar_examen'),
]
