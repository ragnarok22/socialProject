from django import forms


class LoginForm(forms.Form):
    username = forms.TextInput(
        label = 'Usuario',
        required = True,
    );