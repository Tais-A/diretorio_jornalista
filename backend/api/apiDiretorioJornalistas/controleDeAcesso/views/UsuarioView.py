from django.core import paginator
from django.shortcuts import render, redirect
from controleDeAcesso.models import Usuario
from django.core.paginator import Paginator

def list_usuario_view(request, id=None):
    usuario = None
    if id is None and request.user.is_authenticated:
        usuario = Usuario.objects.filter(user=request.user).first()
    elif id is not None:
        usuario = Usuario.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')
    
    context = {
        'usuario': usuario, 

    }

    return render(request, template_name='usuario/usuario.html', context=context, status=200)
