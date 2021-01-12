from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.shortcuts import render
from django.conf import settings as djangoSettings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import login, authenticate

# Create your views here.
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('profiles:home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:login')


class Logout(auth_views.LogoutView):
    success_url = reverse_lazy('accounts:login')
