from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import VerificatorAPI
# Create your views here.

class ApplicationIndexView(TemplateView):
    """
    Shows Index Page of Afip Verificator Application
    """
    template_name="afip/index.html"


class ResultsForQueryView(DetailView):
    """
    Calculates the verification digit and compares that with the response
    of the VerificatorAPI.
    """
    verificator = VerificatorAPI.objects.get(pk=1)
    generator_pattern = (5, 4, 3, 2, 7, 6, 5, 4, 3, 2)

    def digit_generation(request):
        """
        Slice the taken cuil to create a verification digit using the pattern
        to calculate it.
        """
        cuil = cuil[:10]

    def validate_digit():
        """
        Compare the response of the VerificatorAPI with complete cuit
        including the recently created verification digit. If both of them
        have the same value, ResultsForQueryView will return a success message.
        """
        pass

