from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView
from django.core.urlresolvers import reverse

from .models import VerificatorAPI
from .forms import CuilForm 
# Create your views here.

class CuilQueryView(FormView):
    template_name = "afip/verification.html"
    form_class = CuilForm

    def get_success_url(self):
        url = reverse('afip:cuil_query', args=[])
        return "%s?cuil=%s" % (url, self.request.POST['cuil'])

    def get_context_data(self, *args, **kwargs):
        context = super(CuilQueryView, self).get_context_data(**kwargs)
        context['cuil'] = self.request.GET.get('cuil', '')
        return context  
