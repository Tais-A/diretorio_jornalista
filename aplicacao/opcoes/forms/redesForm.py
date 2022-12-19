from django import forms

class RedesForm(forms.Form):
    telegram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Telegram'}), required=False)
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Facebook'}), required=False)
    podcast = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Podcast'}), required=False)
    linkedin = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'LinkedIn'}), required=False)
    twitter = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Twitter'}), required=False)
    site = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder':'Site'}), required=False)