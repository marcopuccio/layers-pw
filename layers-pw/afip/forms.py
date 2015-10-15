from django import forms

class CuilForm(forms.Form):
    cuil = forms.CharField()
