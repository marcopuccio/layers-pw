from django import forms

class CuilForm(forms.Form):
    cuil = forms.CharField(max_length=11)
