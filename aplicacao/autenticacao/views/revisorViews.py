from django.shortcuts import render
from django.http import HttpResponse

def lista_jornalistas_associados_view(request):
  
  return HttpResponse("Você está listando jornalistas associados")

def valida_jornalista_view(request):
  return HttpResponse("Você está detalhado o jornalista para validar")