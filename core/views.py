from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    
class AddLogoView(TemplateView):
    template_name = 'add_logo.html'