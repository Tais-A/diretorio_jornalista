
from django import forms

class LoginForm(forms.Form):
    #email = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'login', 'placeholder':'login'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'form-control', 'placeholder':'Usuário'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), required=True)
        
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuário'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), required=True)