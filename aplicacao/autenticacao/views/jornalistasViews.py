from django.shortcuts import render
from django.http import HttpResponse

def cadastro_jornalista_view(request):
  return HttpResponse("Você está cadastrando dados")

def edita_jornalista_view(request):
  return HttpResponse("Você está detalhado o jornalista para validar")