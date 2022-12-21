from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from autenticacao.models import Jornalista
from autenticacao.models import Associacao

class JornalistaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(JornalistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Jornalista
        fields = [
            'usuario',
            'associacao',
            'nome_de_guerra',
            'cpf',
            'telefone',
            'data_de_nascimento',
            'genero',
            'estado_civil',
        ]

        widgets = {
            'usuario': forms.HiddenInput(),
            'associacao': forms.Select(attrs={'class': 'form-control2'}),
            'nome_de_guerra' : forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nome de Gerra'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'CPF','required':'True'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Telefone'}),
            'data_de_nascimento': forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de nascimento'}),
            'genero': forms.Select(attrs={'class': 'form-control2'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control2'}),
        }

