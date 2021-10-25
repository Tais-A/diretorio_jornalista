from django.core import paginator
from django.shortcuts import redirect, render
from controleDeAcesso.models import Usuario
from django.db.models import Q
from django.core.paginator import Paginator

def list_jornalistas_view(request):
    name = request.GET.get('name')
    city = request.GET.get('city')
    state = request.GET.get('state')

    jornalistas = Usuario.objects
    if name is not None and name != '':
        jornalistas = jornalistas.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))
    else : 
        if city is not None:
            jornalistas = jornalistas.filter(city__id=city)
        elif state is not None:
            jornalistas = jornalistas.filter(city__state=state)
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
    
    return render(request, template_name='jornalista/jornalistas.html', context=context, status=200)

