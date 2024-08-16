from django.urls import path, re_path, include
#
from . import views

app_name = 'user_app'


urlpatterns = [
    path('register-user/', views.AddUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LoguotUserView.as_view(), name='logout'),
]
