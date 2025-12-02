from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Acto 
# Create your views here.

class ActosView(TemplateView):
    template_name = "caida/actos.html"

    def get_context_data(self, **kwargs):
        context = super(ActosView, self).get_context_data(**kwargs)
        context['actos'] = Acto.objects.all()
        return context