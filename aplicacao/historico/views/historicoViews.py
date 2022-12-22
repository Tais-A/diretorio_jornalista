from django.shortcuts import render
from django.http import HttpResponse

from historico.forms.expForm import ExperienceForm

def cadastro_historico(request):
  experienceForm = ExperienceForm()

  context = {
    'form': experienceForm,
  }

  return render(request, template_name="cadastro-historico.html", context=context, status=200)

def edita_historico(request):
  return HttpResponse("Você está editando o historico")

def lista_historico(request):
  return HttpResponse("Você está listando o historico")