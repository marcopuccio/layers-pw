from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView

from .models import VerificatorAPI
from .forms import CuilForm 
# Create your views here.

class ApplicationIndexView(TemplateView):
    """
    Shows Index Page of Afip Verificator Application
    """
    template_name="afip/verification.html"

    def get_context_data(self, **kwargs):
        form = CuilForm()
        context = super(ApplicationIndexView, self).get_context_data(**kwargs)
        context['form'] = form
        return context

class CuilQueryView(FormView):
    template_name = "afip/verification.html"
    form_class = CuilForm
    success_url= "result/"

    def form_valid(self, form):
        return super(CuilQueryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CuilQueryView, self).get_context_data(**kwargs)
        context['success'] = self.success
        return context

class ResultsForQueryView(TemplateView):
    """
    Calculates the verification digit and compares that with the response
    of the VerificatorAPI.
    """
    template_name = "afip/result.html"
