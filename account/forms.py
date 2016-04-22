from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'id': 'username'})
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'})
    )
