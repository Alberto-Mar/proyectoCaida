from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Acto 
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

class ActoCreateView(CreateView):
    model = Acto
    fields = ['nombre', 'tipo', 'fec_inicio']
    def get_success_url(self):
        return reverse_lazy('acto_update', kwargs={'pk': self.object.pk})
    
class ActoUpdateView(UpdateView):
    model = Acto
    fields = ['nombre', 'tipo', 'fec_inicio']
    success_url = reverse_lazy('listado_actos')

class ActoDeleteView(DeleteView):
    model = Acto
    success_url = reverse_lazy('listado_actos')
    
class ListadoActosView(TemplateView):
    template_name = 'caida/listado_actos.html'
    
    def get_context_data(self, **kwargs):
        context = super ().get_context_data(**kwargs)
        q = self.request.GET.get('q', '')
        if q:
            listado_actos = Acto.objects.filter(nombre__icontains=q)
        else:
            listado_actos = Acto.objects.all()
        
        paginador = Paginator(listado_actos, 5)  # 5 actos por página
        pagina = self.request.GET.get('page', 1)
        context["actos"] = paginador.get_page(pagina)
        
        context["q"] = q
        return context

