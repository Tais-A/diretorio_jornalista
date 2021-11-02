from django.contrib.auth.models import User
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404, render
from controleDeAcesso.models import Usuario
from django.core.paginator import Paginator
from controleDeAcesso.forms.UserForm import  UsuarioForm, UserForm

def listar_usuario_view(request, id=None):
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

def editar_usuario(request):
    usuario = get_object_or_404(Usuario, user=request.user)

    emailUnused = True

    message = None

    if request.method == 'POST':
        usuarioForm = UsuarioForm(request.POST, request.FILES, instance=usuario)
        userForm = UserForm(instance=request.user)

        #Verifica se o email que o usuario está usando já existe em outro usuario
        verifyEmail = Usuario.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None

    else:
        usuarioForm = UsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)

    if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
        usuarioForm.save()
        userForm.save()

        message = {'type': 'sucess', 'text': 'Dados atualizados com sucesso'}
    else:
        if request.method == 'POST':
            if emailUnused:
                message = { 'type': 'danger', 'text': 'Dados inválidos'}
            else:
                message = {'type': 'warning', 'test': 'E-mail já usado por outro usuário'}

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }

    return render(request, template_name='user/user.html', context=context, status=200)