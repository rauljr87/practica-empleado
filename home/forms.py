# personalizaciones para los campos de nuestro modelo que se mostrara en el template
from django import forms
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

        # widgets, personalización
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí',
                }
            )
        }

    def clean_cantidad(self):
        """
        valida cantidad
        prefijo clean, obligatorio
        """

        # recuperar objeto cantidad
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')

        return cantidad
