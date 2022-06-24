from django.shortcuts import render
# models
from persona.models import Empleado
from departamento.models import Departamento
# redirect url
from django.urls import reverse_lazy
# vista genérica para trabajar con formulario que no vinculados con un modelo directamente
from django.views.generic.edit import FormView
# form
from .forms import NewDepartamentoForm
# views generic
from django.views.generic import ListView


# LISTVIEW


class DepartamentoListView(ListView):
    template_name = "departamento/lista_departmento.html"
    model = Departamento
    # variable para llamar desde el template
    context_object_name = 'departamentos'


# FORMVIEW


# FormClass
class NewDepartamentoView(FormView):
    """
    Crea un departamento con un empleado por medio de formulario que no depende de un modelo 
    """

    template_name = "departamento/new_departamento.html"
    # uso de formulario
    form_class = NewDepartamentoForm
    # success_url = '/'
    success_url = reverse_lazy('departamento_app:lista_departamento')

    def form_valid(self, form):
        print('******** estamos en el forma valid')
        # instancia departamento
        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name'],
        )
        departamento.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        # creación de objetos en modelo Empleado
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=departamento
        )

        return super(NewDepartamentoView, self).form_valid(form)
