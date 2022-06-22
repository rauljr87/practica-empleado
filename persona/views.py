from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado


# LISTVIEW


# 1.- Listar todos los empleados de la empresa.


class ListAllEmpleados(ListView):
    """ Lista todos los empleados de la empresa """

    template_name = 'persona/list_all.html'
    # se comenta model ya que se sobre escribe el método get_queryset
    # model = Empleado
    # paginación por bloques de 4
    paginate_by = 4
    ordering = 'first_name'
    # variable para el template
    context_object_name = 'empleados'

    def get_queryset(self):
        """ Captura el texto enviado por el input a través del form, method GET REQUEST """

        # kword, id capturado del GET REQUEST enviado por el input del formulario en el template
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            # filtro queryset por full_name a modelo Empleado
            first_name__icontains=palabra_clave
        )

        return lista


# 2.- Listar todos los empleados que pertenecen a una área de la empresa


class ListByAreaEmpleado(ListView):
    """ Lista todos los empleados de la empresa por su área """

    template_name = 'persona/list_by_area.html'
    # filtro a través de un queryset
    # queryset = Empleado.objects.filter(
    #    # filtro queryset por short_name a departamento
    #    departamento__short_name='informatica',
    # )

    # optimizando el filtro
    def get_queryset(self):
        """ Retorna lista filtrando los empleados por departamento """

        # pasamos, mediante kwargs, la variable declarada en la url para aplicar filtro por departamento
        area = self.kwargs['short_name']

        lista = Empleado.objects.filter(
            # filtro queryset por short_name a departamento del modelo Empleado
            departamento__short_name=area
        )

        return lista


# 3.- Listar empleados por trabajo.


class ListByJobs(ListView):
    """ Lista todos los empleados de la empresa por trabajo """

    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        """ Retorna lista filtrando los empleados por trabajo """

        # pasamos, mediante kwargs, la variable declarada en la url para aplicar filtro por trabajo
        job = self.kwargs['job']

        lista = Empleado.objects.filter(
            # filtro queryset por job del modelo Empleado
            job=job
        )

        return lista


# 4.- Listar empleados por palabra clave.


class ListEmpleadosByKword(ListView):
    """ Lista todos los empleados por palabra clave """

    template_name = 'persona/list_by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        """ Captura el texto enviado por el input a través del form, method GET REQUEST """

        print('######################')

        # kword, id capturado del GET REQUEST enviado por el input del formulario en el template
        palabra_clave = self.request.GET.get("kword",)

        print('===========', palabra_clave)

        lista = Empleado.objects.filter(
            # filtro queryset por first_name a modelo Empleado
            first_name=palabra_clave
        )

        print('##################')
        print('Lista resultado:', lista)

        return lista


# 5.- Listar habilidades de un empleado.


class ListHabilidadesEmpleado(ListView):
    """ Lista todos los empleados por habilidades """

    template_name = 'persona/list_by_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        """ Captura el texto enviado por el input a través del form, method GET REQUEST """

        # kword, id capturado del GET REQUEST enviado por el input del formulario en el template
        palabra_clave = self.request.GET.get("habilidad")

        # recupera un único objeto empleado
        empleado = Empleado.objects.get(
            # método get para obtener listado de habilidades por id
            id=palabra_clave
        )

        print("#############")
        print(empleado.habilidades.all())

        return empleado.habilidades.all()


# DETAILVIEW


class EmpleadoDetailView(DetailView):
    """ Muestra detalles de un empleado """

    template_name = "persona/detail_empleado.html"
    model = Empleado

    def get_context_data(self, **kwargs):
        """ envía alguna variable extra al template """

        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # variable de aumento en el template
        context['titulo'] = 'Empleado del mes'

        return context


# TEMPLATEVIEW


class SuccessView(TemplateView):
    """ Muestra una página una vez creado un registro """

    template_name = "persona/success.html"


class InicioTemplateView(TemplateView):
    """ Vista que carga la página de inicio """

    template_name = 'inicio.html'


# CREATEVIEW


class EmpleadoCreateView(CreateView):
    """ Crea registro de empleado """

    template_name = 'persona/add_empleado.html'
    model = Empleado
    # field específicos
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    # todos los fields
    # fields = ('__all__')
    # url cuando form exitoso, misma page
    # success_url = '.'
    # url cuando form exitoso
    # success_url = '/success'
    # url cuando form exitoso, name
    success_url = reverse_lazy('persona_app:success')

    # proceso previo al guardado de datos
    def form_valid(self, form):
        """ crear full name a partir de first_name y last_name """

        # instancia temporalmente la variable empleado
        empleado = form.save(commit=False)
        print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


# UPDATEVIEW


class EmpleadoUpdateView(UpdateView):
    """ Actualiza registro de empleado """

    template_name = "persona/update_empleado.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:success')

    # procesos previos al guardado de datos
    def post(self, request, *args, **kwargs):
        """  """

        self.object = self.get_object()

        print('######## METODO POST ########')
        print('*****************************')
        print(request.POST)
        print(request.POST['last_name'])

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """  """

        print('######## METODO FORM VALID ########')
        print('#############################')

        return super(EmpleadoUpdateView, self).form_valid(form)


# DELETEVIEW


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete_empleado.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:success')
