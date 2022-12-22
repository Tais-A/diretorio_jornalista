from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.conf import settings

from autenticacao.forms.authForm import LoginForm, RegisterForm

def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect('/')
            else:
                message = {
                    'type':'danger',
                    'text':'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registre agora',
        'link_href': '/register'
    }

    return render(request, template_name='login.html', context=context, status=200)

def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este username!'}
            elif verifyEmail is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este email!'}
            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = {'type': 'success', 'text': 'Conta criada com sucesso!' }
                    login(request, user)
                    return redirect('/jornalista/cadastro')            

                else:
                    message = {'type':'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}

        
    
    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href':'/login'
    }

    return render(request, template_name='login.html', context=context, status=200)

def logout_view(request):
    logout(request)
    return redirect('/login')