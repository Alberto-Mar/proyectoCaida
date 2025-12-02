from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name="caida/home.html"


# Create your views here.
