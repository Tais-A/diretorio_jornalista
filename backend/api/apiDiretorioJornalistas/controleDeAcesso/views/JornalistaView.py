from django.core import paginator
from django.shortcuts import redirect, render
from controleDeAcesso.models import Usuario, Confiabilidade
from controleDeAcesso.forms.JornalistaForm import ConfiabilidadeForm
from django.db.models import Q
from django.core.paginator import Paginator

def list_jornalistas_view(request):
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
    
    return render(request, template_name='jornalista/jornalistas.html', context=context, status=200)

def nota_jornalista(request, jornalista_id=None):
    jornalista = Usuario.objects.filter(user__id=jornalista_id).first()
    confiabilidade = Confiabilidade.objects.filter(user=request.user, user_rated=jornalista.user).first()
    message = None
    initial = {'user': request.user, 'user_rated': jornalista.user}

    if request.method == 'POST':
        confiabilidadeForm = ConfiabilidadeForm(request.POST, instance=confiabilidade, initial=initial)
    else: 
        confiabilidadeForm = Confiabilidade(isntance=confiabilidade, initial=initial)

        if confiabilidadeForm.is_valid():
            confiabilidadeForm.save()
            message = {'type': 'sucess', 'text': 'Avaliação salva com sucesso'}
        else:
            if request.method == 'POST':
                message = {'type': 'danger', 'text':'Erro ao salvar avaliação'}
    context = {
        'confiabilidadeForm' : confiabilidadeForm,
        'jornalista': jornalista,
        'message': message
    }

    return render(request, template_name='jornalista/rating.html', context=context, status=200)