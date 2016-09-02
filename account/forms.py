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

    def get_password(self):
        return self.cleaned_data['password']

    def get_user(self):
        return self.cleaned_data['username']
