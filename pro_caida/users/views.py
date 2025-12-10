from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Hermano

# Create your views here.

class HermanoView(TemplateView):
    template_name="caida/inicio_hermano.html"
    
class AdminView(TemplateView):
    template_name="caida/inicio_admin.html"

class ListaHermanosView(ListView):
    paginate_by = 10
    model = Hermano
    template_name = "caida/lista_hermanos.html"

class UserCreateView(CreateView):
    model = Hermano
    fields = ['nombre_completo', 'numero_hermano', 'dni', 'fec_nacimiento', 'foto', 'cargo_junta']
    success_url = reverse_lazy('login')  
    
class UserUpdateView(UpdateView):
    model = Hermano
    fields = ['nombre_completo', 'numero_hermano', 'dni', 'fec_nacimiento', 'foto', 'cargo_junta']
    success_url = reverse_lazy('home')   

class CrearHermanoView(TemplateView):
    template_name="caida/crear_hermano.html"