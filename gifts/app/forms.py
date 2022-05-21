from django import forms 
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):

    name = forms.CharField(
            label='', 
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    surname = forms.CharField(
            label='', 
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )

    email = forms.EmailField(
            label='',
            widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    password = forms.CharField(
            label='', 
            max_length=120,
            widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'})
    )

    password2 = forms.CharField(
            label='', 
            max_length=120,
            widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'})

    )

    #def clean(self):
    #    cleaned_data = super().clean()
    #    password = cleaned_data.get('password')
    #    password2 = cleaned_data.get('password2')
    #    if password != password2:
    #        raise forms.ValidationError('Hasła nie są takie same!')

class LoginForm(forms.Form):

    email = forms.EmailField(
            label='',
            widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    password = forms.CharField(
            label='', 
            max_length=120,
            widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'})
    )
