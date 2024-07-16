from django.shortcuts import render
#
from django.views.generic import FormView, View
#
from .forms import LoginForm
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

