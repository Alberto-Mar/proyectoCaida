from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Hermano

class LoginView(TemplateView):
    template_name="caida/login.html"
    
class ErrorView(TemplateView):
    template_name="error.html"
    

    
class CrearActoView(TemplateView):
    template_name="caida/crear_acto.html"


# Create your views here.
