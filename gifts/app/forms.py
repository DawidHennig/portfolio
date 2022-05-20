from django import forms 

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

        password = forms.CharField(label='', 
            max_length=120,
            widget=forms.TextInput(attrs={'placeholder': 'Hasło'})

        )
        password2 = forms.CharField(label='', 
            max_length=120,
            widget=forms.TextInput(attrs={'placeholder': 'Powtórz hasło'})

        )
