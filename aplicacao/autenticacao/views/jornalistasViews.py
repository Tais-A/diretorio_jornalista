from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404

from autenticacao.forms.jornalistaForm import JornalistaForm
from opcoes.forms.redesForm import RedesForm
from autenticacao.models import Jornalista

def cadastro_jornalista_view(request, id=None):
  jornalista = None
  if id is None and request.user.is_authenticated:
    jornalista = Jornalista.objects.filter(usuario=request.user).first()
  elif id is not None:
    jornalista = Jornalista.objects.filter(usuario__id=id).first()
  elif not request.user.is_authenticated:
    return redirect(to='/')

  
  redesForm = RedesForm()
  mensagem = None

  if request.method == 'POST':
    jornalistaForm = JornalistaForm(request.POST, request.FILES, instance=jornalista)
  else:
    jornalistaForm = JornalistaForm(instance=jornalista)

  if jornalistaForm.is_valid():
    jornalistaForm.save()
    mensagem = { 'text': 'Dados atualizados com sucesso '}
  else:
    mensagem = { 'text': 'Dados inválidos '}

  context = {
    'form': jornalistaForm,
    'redes': redesForm,
    'id': id,
    'mensagem': mensagem,
  }

  
  return render(request, template_name='jornalistas/cadastro-jornalistas.html', context=context, status=200)


def dados_jornalista_view(request, id=None):
  jornalista = None
  if id is None and request.user.is_authenticated:
    jornalista = Jornalista.objects.filter(usuario=request.user).first()
  elif id is not None:
    jornalista = Jornalista.objects.filter(usuario__id=id).first()
  elif not request.user.is_authenticated:
    return redirect(to='/')

def edita_jornalista_view(request):
  jornalista = get_object_or_404(Jornalista, usuario=request.user)
  # if id is None and request.user.is_authenticated:
  #   jornalista = Jornalista.objects.filter(usuario=request.user).first()
  if request.method == 'POST':
    jornalistaForm = JornalistaForm(request.POST, instance=jornalista)
      # redesForm = RedesForm(instance=request.redes)
  else:
    jornalistaForm = JornalistaForm(instance=jornalista)
      # redesForm = RedesForm(instance=request.redes) 

  if jornalistaForm.is_valid(): 
    jornalistaForm.save()
    message = { 'type': 'sucess', 'texte': 'Dados atualizados com sucesso'}
  else:
    message = { 'type': 'danger', 'texte': 'Dados inválidos'}

  context = {
    'form': jornalistaForm,
      # 'redes': redesForm,
    'id': id,
  }

  jornalista.save()
  return redirect(home_view)
  

def salvar(request):
  pass
  