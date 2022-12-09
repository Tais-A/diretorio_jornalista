from django.shortcuts import render
from django.http import HttpResponse

from autenticacao.forms.jornalistaForm import JornalistaForm
from opcoes.forms.redesForm import RedesForm

def cadastro_jornalista_view(request, id):
  jornalistaForm = JornalistaForm()
  redesForm = RedesForm()

  context = {
    'form': jornalistaForm,
    'redes': redesForm,
    'id': id,
  }

  return render(request, template_name='jornalistas/cadastro-jornalistas.html', context=context, status=200)

def edita_jornalista_view(request, id=None):
  jornalista = None
  if id is None and request.user.is_authenticated:
    jornalista = Jornalista.objects.filter(usuario=request.user).first()
    return HttpResponse("ser")

  return HttpResponse("Você está detalhado o jornalista para validar")