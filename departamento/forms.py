"""
- Formularios tipo ModelForm, que dependen de un modelo en particular.
- Formularios simples, que no dependen de un modelo en específico.
"""


from django import forms


# SIMPLE FORM


# formulario que no depende de un modelo en específico
class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50, required=True)
    short_name = forms.CharField(max_length=50, required=True)
