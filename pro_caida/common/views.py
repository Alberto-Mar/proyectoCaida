from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Hermano

class LoginView(TemplateView):
    template_name="caida/login.html"
    
class ErrorView(TemplateView):
    template_name="error.html"
    
class HermanoView(TemplateView):
    template_name="caida/inicio_hermano.html"
    
class AdminView(TemplateView):
    template_name="caida/inicio_admin.html"
    
class UserCreateView(CreateView):
    model = Hermano
    fields = ['nombre_completo', 'dni', 'fec_nacimiento', 'foto', 'cargo_junta']  
    success_url = reverse_lazy('login')  
    
class UserUpdateView(UpdateView):
    model = Hermano
    fields = ['nombre_completo', 'dni', 'fec_nacimiento', 'foto', 'cargo_junta']
    success_url = reverse_lazy('home')   

class CrearHermanoView(TemplateView):
    template_name="caida/crear_hermano.html"
    
class CrearActoView(TemplateView):
    template_name="caida/crear_acto.html"


# Create your views here.
