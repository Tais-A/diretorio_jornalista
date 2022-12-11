from django import forms

class JornalistaForm(forms.Form):
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
