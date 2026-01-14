from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from users.models import Hermano

class LoginFormView(LoginView):
    template_name="caida/login.html"
    next_page = reverse_lazy('inicio_hermano')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('inicio_hermano')
        return super().dispatch(request, *args, **kwargs)
    
class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ErrorView(TemplateView):
    template_name="error.html"
    

    
class CrearActoView(TemplateView):
    template_name="caida/crear_acto.html"


# Create your views here.
