from django.shortcuts import render
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name="caida/login.html"
    
class ErrorView(TemplateView):
    template_name="error.html"
    
class HermanoView(TemplateView):
    template_name="caida/inicio_hermano.html"
    
class AdminView(TemplateView):
    template_name="caida/inicio_admin.html"
    
class CrearHermanoView(TemplateView):
    template_name="caida/crear_hermano.html"
    
class CrearActoView(TemplateView):
    template_name="caida/crear_acto.html"


# Create your views here.
