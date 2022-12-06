from django import forms

class LoginForm(forms.Form):
    #email = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'login', 'placeholder':'login'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'form-control', 'placeholder':'Usuário'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), required=True)
        
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuário'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), required=True)

class DadosForm(forms.Form):
    nacionalidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nacionalidade'}))
    dataNascimento = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de nascimento'}), required=True)
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'CPF'}), required=True)
    telefone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Telefone'}), required=True)
    etnia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Etnia'}))
    localNascimento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Local de nascimento'}), required=True)
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Nome Completo'}), required=True)
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Cidade/Estado Residencial'}), required=True)
    registro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Registro'}), required=False)
    diploma = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control2', 'placeholder':'Diploma'}), required=False)
    area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Área/Especialidade'}), required=False)
    dataFormacao = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de Formatura'}), required=True)
