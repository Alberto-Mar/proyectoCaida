from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Hermano
from .forms import HermanoForm

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
    form_class = HermanoForm
    success_url = reverse_lazy('login')  
    
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['dni'])
        usuario.save()
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = Hermano
    fields = ['nombre_completo', 'numero_hermano', 'dni', 'fec_nacimiento', 'foto', 'cargo_junta']
    success_url = reverse_lazy('home')   

class CrearHermanoView(TemplateView):
    template_name="caida/crear_hermano.html"
    
class GestionHermanosView(TemplateView):
    template_name = "caida/gestion_hermanos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Enviamos todos los hermanos para que JS genere las cards
        context['hermanos'] = Hermano.objects.all().order_by('numero_hermano')
        return context

    def post(self, request, *args, **kwargs):
        # Determinamos si es borrar o guardar (crear/editar) mediante un campo oculto 'accion'
        accion = request.POST.get('accion')
        email_pk = request.POST.get('email')

        if accion == 'borrar':
            hermano = get_object_or_404(Hermano, email=email_pk)
            hermano.delete()
            messages.warning(request, "Hermano eliminado correctamente.")
        
        elif accion == 'guardar':
            # El email es la PK, si existe actualiza, si no, crea.
            hermano, created = Hermano.objects.update_or_create(
                email=email_pk,
                defaults={
                    'nombre': request.POST.get('nombre'),
                    'dni': request.POST.get('dni'),
                    'numero_hermano': request.POST.get('numero_hermano'),
                    'tipo_hermano': request.POST.get('tipo_hermano'),
                    'cargo_junta': request.POST.get('cargo_junta') == 'on'
                }
            )
            if created:
                hermano.set_password(request.POST.get('dni'))
                hermano.save()
            
            messages.success(request, f"Hermano {'registrado' if created else 'actualizado'} con éxito.")

        return redirect('gestion_hermanos') 