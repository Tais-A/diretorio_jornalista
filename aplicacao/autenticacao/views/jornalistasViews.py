from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from autenticacao.forms.jornalistaForm import JornalistaForm
from opcoes.forms.redesForm import RedesForm
from autenticacao.models import Jornalista, Associacao
from opcoes.models import Genero, EstadoCivil


@login_required
def cadastro_jornalista_view(request):

    initial = {'usuario':request.user}
    message = None
    redes = RedesForm()

    if request.method == 'POST':
        jornalistaForm = JornalistaForm(request.POST, initial=initial)
        try:
          dados_form = jornalistaForm.data

          jornalista = Jornalista()

          jornalista.usuario=request.user
          jornalista.associacao_id=dados_form['associacao']
          jornalista.nome_de_guerra=dados_form['nome_de_guerra']
          jornalista.cpf=dados_form['cpf']
          jornalista.telefone=dados_form['telefone']
          jornalista.data_de_nascimento=dados_form['data_de_nascimento']
          jornalista.genero_id=dados_form['genero']
          jornalista.estado_civil_id=dados_form['estado_civil']

             

          jornalista.save()

          message = {'type': 'sucess', 'text': 'Dados atualizados com sucesso'}
          redirect('/')
        except Exception as e:
          message = { 'type': 'danger', 'text': 'Erro ao salvar jornalista. Descrição: %s' %e }

    else:
        jornalistaForm = JornalistaForm(initial=initial)


    context = {
        'form': jornalistaForm,
        'redes': redes,
        'message': message
    }

    return render(request, template_name='jornalistas/cadastro-jornalista.html', context=context, status=200)




def dados_jornalista_view(request, id=None):
  if id is not None:
    jornalista = Jornalista.objects.filter(usuario__id=id)
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

    message = { 'type': 'sucess', 'text': 'Dados atualizados com sucesso'}
    
    return redirect('/')

  else:
    message = { 'type': 'danger', 'text': 'Dados inválidos'}

  context = {
    'form': jornalistaForm,
      # 'redes': redesForm,
    'id': id,
  }

  jornalista.save()

  return redirect(home_view)
  
def salvar():
  pass

def get_logged_user(request):
    return request.user.user_profile