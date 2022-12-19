from django import forms

class ExperienceForm(forms.Form):
    empresa = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Empresa'}))
    local = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Local'}))
    veiculo = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Veiculo'}), required=True)
    cargo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Cargo'}), required=True)
    dataInicio = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de Inicio'}), required=True)
    dataFim = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder':'Data de Encerramento'}))
    referencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Referência'}), required=True)
    contatoReferencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contato da Referência'}), required=True)
    descricao = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Empresa'}))