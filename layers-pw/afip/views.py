from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ApplicationIndexView(TemplateView):
    template_name="afip/index.html"
