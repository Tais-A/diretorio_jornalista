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
        fields = '__all__'

        widgets = {
            'usuario': forms.HiddenInput(),
            'criado_em': forms.HiddenInput(),
            'atualizado_em': forms.HiddenInput(),
            'aprovado': forms.HiddenInput(),
            'associacao': forms.Select(attrs={'class': 'form-control2'}),
            'nome_de_guerra' : forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nome de Gerra'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'CPF','required':'True'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Telefone'}),
            'data_de_nascimento': forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de nascimento'}),
            'genero': forms.Select(attrs={'class': 'form-control2'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control2'}),


            
            # 'nacionalidade' :forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nacionalidade'})),
            # 'data_de_nascimento': forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de nascimento'}), required=True),
            # localNascimento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Local de nascimento'}), required=True)
            # nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nome Completo'}), required=True)
            # cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Cidade/Estado Residencial'}), required=True)
            # registro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Registro'}), required=False)
            # diploma = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control2', 'placeholder':'Diploma'}), required=False)
            # area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Área/Especialidade'}), required=False)
            # dataFormacao = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de Formatura'}),required=True)

        }

