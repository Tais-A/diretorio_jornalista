from django.core import paginator
from django.shortcuts import redirect, render
from publicacao.models import Artigo
from publicacao.models import *
from publicacao.forms.PublicacaoForm import ArtigoForm
from django.db.models import Q
from django.core.paginator import Paginator


def list_artigos_view(request):
    titulo = request.GET.get('titulo')
    veiculo = request.GET.get('veiculo')
    descricao = request.GET.get('descricao')

    artigos = Artigo.objects

    if titulo is not None and titulo != '':
        artigos = artigos.filter(titulo__id=titulo)
    elif veiculo is not None:
        artigos = artigos.filter(veiculo = veiculo)

    if len(artigos) > 0:
        paginator = Paginator(artigos, 8)
        page = request.GET.get('page')
        artigos = paginator.get_page(page)
    
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'artigos': artigos,
        'paramenters': parameters
    }

    return render(request, template_name='usuario/usuario.html', context=context, status=200)

# def add_artigo(request):
#     page = request.POST.get("page")
#     titulo = request.POST.get("titulo")
#     veiculo = 