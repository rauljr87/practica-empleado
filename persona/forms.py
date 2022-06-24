"""
- Formularios tipo ModelForm, que dependen de un modelo en particular.
- Formularios simples, que no dependen de un modelo en específico.
"""

# importar formulario de django
from django import forms
# importar modelo para el formulario
from .models import Empleado
# importar este formulario en las views de la app


class EmpleadoForm(forms.ModelForm):
    """ Genera un formulario """

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )
        # Personalización
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }

# se debe importar el formulario en las views de la app
