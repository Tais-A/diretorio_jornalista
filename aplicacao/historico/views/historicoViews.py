from django.shortcuts import render
from django.http import HttpResponse

def cadastro_historico(request):
  return HttpResponse("Você está na página de cadastro de historico")

def edita_historico(request):
  return HttpResponse("Você está editando o historico")

def lista_historico(request):
  return HttpResponse("Você está listando o historico")