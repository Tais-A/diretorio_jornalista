from django import forms
from django.forms import ModelForm, fields, widgets
from controleDeAcesso.models.Confiabilidade import Confiabilidade

class ConfiabilidadeForm(ModelForm):
    class Meta:
        model = Confiabilidade
        fields = ['user', 'user_rated', 'value','opinion']
        widgets = {
            'user': forms.HiddenInput(),
            'user_rated': forms.HiddenInput(),
            'value': forms.NumberInput(attrs={'class': "form-control"}),
            'opinion': forms.Textarea(attrs={'class': "form-control", "rows":4}),
        }