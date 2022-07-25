from django.shortcuts import render
from django.core import paginator
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse


def home_view(request):
    return render(request, template_name='index.html', status=200)


def lista_jornalistas_view(request):
    name = request.GET.get('name')
    cidade = request.GET.get('cidade')
    estado = request.GET.get('estado')

    jornalistas = Usuario.objects
    if name is not None and name != '':
        jornalistas = jornalistas.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))
    else : 
        if cidade is not None:
            jornalistas = jornalistas.filter(cidade__id=cidade)
        elif estado is not None:
            jornalistas = jornalistas.filter(cidade__estado=estado)
    if len(jornalistas) > 0:
        paginator = Paginator(jornalistas, 8)
        page = request.GET.get('page')
        jornalistas = paginator.get_page(page)
    
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'jornalistas': jornalistas,
        'parameters': parameters
    }
    
    return render(request, template_name='jornalistas.html', context=context, status=200)