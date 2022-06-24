"""
- Formularios tipo ModelForm, que dependen de un modelo en particular.
- Formularios simples, que no dependen de un modelo en específico.
"""

# Personalizaciones para los campos de nuestro modelo que se mostrara en, el template.
# Importar formulario de django
from django import forms
# importar modelo para el formulario
from .models import Prueba


# MODEL FORMS


class PruebaForm(forms.ModelForm):
    """ Custom form """

    class Meta:
        model = Prueba
        # fields = ('__all__')
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        # personalización de attributes
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí',
                }
            )
        }

    def clean_cantidad(self):
        """
        - Validación de cantidad
        - Prefijo clean, obligatorio
        """

        # recuperar objeto cantidad
        cantidad = self.cleaned_data['cantidad']
        # validación de cantidad
        if cantidad < 10:
            # dato incorrecto
            raise forms.ValidationError('Ingrese un número mayor a 10')

        return cantidad

# importar este formulario en las views de la app
