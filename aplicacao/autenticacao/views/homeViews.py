from django.shortcuts import render
from django.core import paginator
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse

from ..models import Jornalista

def home_view(request):
    context = {}
    jornalistas = Jornalista.objects.all()

    if (request.GET.get('inicial') != None):            # Verifica se a pesquisa foi pelo glossario
        filtro = []
        for i in jornalistas:                           
            if str(i)[0] == request.GET.get('inicial'): # Lista os Jornalistas com a inicial escolhida.
                filtro.append(i)

        context = {
            'form': filtro                              # Envia para Form os jornalistas encontrados.
        }

    if request.GET.get('name') != None:                 # Verifica se a pesquisa foi pelo nome.
        name = request.GET.get('name')
        jornalistas = jornalistas.filter(nome_de_guerra__contains=name)     # Filta os jornalistas pelo nome.

        context = {
            'form': jornalistas                         # Envia para Form os jornalistas encontrados.
        }

    return render(request, template_name='index.html', context=context, status=200)


def lista_jornalistas_view(request):
    name = request.GET.get('name')
    cidade = request.GET.get('cidade')
    estado = request.GET.get('estado')

    jornalistas = Usuario.object
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