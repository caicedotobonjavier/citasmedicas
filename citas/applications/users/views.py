from django.shortcuts import render
#
from .models import User
#
from django.views.generic import FormView, View
#
from .forms import LoginForm, AddUserForm
#
from django.contrib.auth import login, logout, authenticate
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
# Create your views here.


class LoginUserView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(email=email, password=password)

        login(self.request, user)

        return super(LoginUserView, self).form_valid(form)



class LoguotUserView(View):

    def post(self, request, *args, **kwargs):

        logout(request)

        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )


class AddUserView(FormView):
    template_name = 'users/register_user.html'
    form_class = AddUserForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            full_name = form.cleaned_data['full_name'],
            cedula = form.cleaned_data['cedula'],
            genero = form.cleaned_data['genero'],
            cargo = form.cleaned_data['cargo'],
            telefono = form.cleaned_data['telefono'],
        )
        return super(AddUserView, self).form_valid(form)
    