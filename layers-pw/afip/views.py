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
        url = reverse('cuil_query')
        return "%s?cuil=%s" % (url, self.request.POST['cuil'])

    def form_valid(self, form, *args, **kwargs):
        self.cuil = form.cleaned_data.get('cuil')
        context = super(CuilQueryView, self).get_context_data(**kwargs)
        context['cuil'] = self.cuil
        return super(CuilQueryView, self).form_valid(form, *args, **kwargs)
