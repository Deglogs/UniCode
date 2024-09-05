
from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import *
from django.contrib.auth import logout
from django.urls import *
from .forms import * 
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def logout_user(request):
    logout(request)
    return redirect('home')