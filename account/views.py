from django.shortcuts import render
from django.views.generic import ListView


class LoginView(ListView):
    template_name = 'account/login.html'
