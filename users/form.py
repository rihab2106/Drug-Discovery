from django import forms
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password', "isPremium"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),

        }
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))