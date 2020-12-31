from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.shortcuts import render
from django.conf import settings as djangoSettings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms


# Create your views here.
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('profiles:home')
    template_name = 'accounts/signup.html'


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('classes:home')


class Logout(auth_views.LogoutView):
    success_url = reverse_lazy('classes:home')
