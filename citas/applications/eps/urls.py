from django.urls import path, re_path, include
#
from . import views

app_name = 'eps_app'


urlpatterns = [
    path('agregar-eps/', views.AgregarEpsView.as_view(), name='agregar_eps'),
    path('lista-eps/', views.ListaEpsView.as_view(), name='lista_eps'),
]
