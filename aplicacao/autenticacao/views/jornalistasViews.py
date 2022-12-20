from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db.models import Q

from autenticacao.forms.jornalistaForm import JornalistaForm
from opcoes.forms.redesForm import RedesForm
from autenticacao.models import Jornalista

@login_required
def add_jornalista(request):
  return render(request, 'add_jornalista.html', {'logged_profile':get_logged_user(request)})


class AddJornalistaView(View):
  template_name = 'add_jornalista.html'
  def get(self, request, *args, **kwargs):
    return HttpResponse(request.user.id)

  def post(self, request, *args, **kwargs):
    jornalistaForm = JornalistaForm(request.POST)

    if jornalistaForm.is_valid():
      dados_form = form.data

      jornalista = Jornalista (
            usuario =request.user,
            associacao=dados_form['associacao'],
            nome_de_guerra=dados_form['nome_de_guerra'],
            cpf=dados_form['cpf'],
            telefone=dados_form['telefone'],
            data_de_nascimento=dados_form['data_de_nascimento'],
            genero=dados_form['genero'],
            estado_civil=dados_form['estado_civil'],
      )

      jornalista.save()

      return redirect('/')

    return render(request, self.template_name, {'form': jornalistaForm})



def cadastro_jornalista_view(request):
    
    message = None

    if request.method == 'POST':
        jornalista = Jornalista()
        jornalistaForm = JornalistaForm(request.POST, instance=jornalista)
        # userForm = UserForm(instance=request.user)

    else:
        jornalista = Jornalista.objects.filter(usuario=request.user).first()
        jornalistaForm = JornalistaForm(instance=jornalista)
        # userForm = UserForm(instance=request.user)

    # if jornalistaForm.is_valid() and userForm.is_valid() and emailUnused:

    if jornalistaForm.is_valid():
        dados_form = form.data

        jornalista = Jornalista (
                usuario=request.user,
                associacao=dados_form['associacao'],
                nome_de_guerra=dados_form['nome_de_guerra'],
                cpf=dados_form['cpf'],
                telefone=dados_form['telefone'],
                data_de_nascimento=dados_form['data_de_nascimento'],
                genero=dados_form['genero'],
                estado_civil=dados_form['estado_civil'],
          )

        jornalista.save()
        print(jornalista.pk)
 
        # userForm.save()

        message = {'type': 'sucess', 'text': 'Dados atualizados com sucesso'}
        redirect('/')
    else:
        message = { 'type': 'danger', 'text': 'Dados inválidos'}


    context = {
        'form': jornalistaForm,
        # 'userForm': userForm,
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

    message = { 'type': 'sucess', 'texte': 'Dados atualizados com sucesso'}
    
    return redirect('/')

  else:
    message = { 'type': 'danger', 'texte': 'Dados inválidos'}

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