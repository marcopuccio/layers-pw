from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse

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


class ResultsForQueryView(TemplateView):
    """
    Calculates the verification digit and compares that with the response
    of the VerificatorAPI.
    """

    template_name = 'afip/verification.html'
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            return HttpResponse("posted")
        return context
    
    def get_context_data(self, **kwargs):
        context = super(ResultsForQueryView, self).get_context_data(**kwargs)
        form = CuilForm(self.request.POST or None)
        context['form'] = form
        return context



