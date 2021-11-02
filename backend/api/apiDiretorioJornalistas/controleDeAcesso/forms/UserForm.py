from django import forms
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.models import User
from controleDeAcesso.models.Usuario import Usuario


class UsuarioForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.funcao != 1:
            del self.fields['funcao']
    
    class Meta:
        model = Usuario
        fields = ('user', 'funcao', 'data_nascimento', 'imagem', 'raca_etnia', 'genero','estado_civil','cidade') #pontos que seram usados, usar __all__ se for todos ou exclude para excluir algum em especifico

        widgets = {
            'user': forms.HiddenInput(),
            'funcao': forms.Select(attrs={'class': "form-control"}),
            'data_nascimento': forms.DateInput(attrs={'class': "form-control", "type": "date"}),
            'image': forms.FileInput(attrs={'class':"form-control"}),
            'raca_etnia': forms.Select(attrs={'class':"form-control"}),
            'genero': forms.Select(attrs={'class':"form-control"}),
            'estado_civil': forms.TextInput(attrs={'class':"form-control"}),
            'cidade': forms.Select(attrs={'class':"form-control"}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"})
        }
