from django import forms

class CuilForm(forms.Form):
    cuil = forms.CharField(label="Ingrese su CUIL",
                           error_messages= {
                               'required': 'Este campo es obligatorio',
                               'min_length': 'Debe ingresar minimo 11 digitos',
                               },
                           min_length=11,
                           max_length=11,
                           )
