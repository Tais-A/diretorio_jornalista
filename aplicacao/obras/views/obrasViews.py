from django.shortcuts import render
from django.http import HttpResponse

def cadastro_obra(request):
  return HttpResponse("Você está na página de cadastro de obra")

def edita_obra(request):
  return HttpResponse("Você está na página de edicao de obra")

def listar_obras(request):
  return HttpResponse("Você está listando as obras")