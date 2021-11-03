from django import forms
from django.forms import ModelForm, fields, widgets
from publicacao.models.Artigo import Artigo

class ArtigoForm(ModelForm):

    class Meta:
        model = Artigo
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'titulo': forms.TextInput(attrs={'class': "form-control"}),
            'veiculo': forms.Select(attrs={'class': "form-control"}),
            'descricao': forms.Textarea(attrs={'class': "form-control"}),
        }