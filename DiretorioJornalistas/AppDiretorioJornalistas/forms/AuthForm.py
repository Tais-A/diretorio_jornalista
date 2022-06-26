
from django import forms

class LoginForm(forms.Form):
    #email = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'login', 'placeholder':'login'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'caixa-login','class': 'form-control', 'placeholder':'Login'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), required=True)
        
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)