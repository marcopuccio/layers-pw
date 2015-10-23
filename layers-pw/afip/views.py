from django.shortcuts import render
from django.views.generic import FormView
from django.core.urlresolvers import reverse

from .models import VerificatorAPI
from .forms import CuilForm 
# Create your views here.

class CuilQueryView(FormView):
    """
    Render a form, calculates a verification number and compares with the
    response of a Verificator pseudo API and returns a context variable with
    a message if true or false
    """
    template_name = "afip/verification.html"
    form_class = CuilForm

    def get_success_url(self):
        url = reverse('afip:cuil_query', args=[])
        return "%s?cuil=%s" % (url, self.request.POST['cuil'])

    def get_context_data(self, *args, **kwargs):
        context = super(CuilQueryView, self).get_context_data(**kwargs)
        context['cuil'] = self.request.GET.get('cuil', '')
        if self.request.GET:
            context['verification'] = self.digit_validation()
        return context

    def digit_creation(self):
        """
        Calculates the real verification Cuil/Cuit number
        """
    	pattern = (5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
        cuil = self.request.GET.get('cuil')[:10]
        digit = 0

        for x, y in zip(cuil, pattern):
            digit = digit + (int(x) * y)

        rest = digit % 11
        digit = 11 - rest

        return digit

    def digit_validation(self):
        """
        Validates the digit created against the API response
        """
        cl = self.request.GET.get('cuil')
        API = VerificatorAPI.objects.get(pk=1)
        api_resp = str(API.add_one(int(cl)))
        created_digit = cl[:10] + str(self.digit_creation())
        if created_digit == api_resp:
            return "Cuil Correcto"
        else:
            return "Cuil Incorrecto"        
