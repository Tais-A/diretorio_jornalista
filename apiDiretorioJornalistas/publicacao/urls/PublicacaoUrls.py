from django.urls import path

from publicacao.views.PublicacaoView import list_artigos_view

urlpatterns = [
    path("", list_artigos_view, name='artigos')    
]
