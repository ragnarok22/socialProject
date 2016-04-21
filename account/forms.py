from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field
from crispy_forms.bootstrap import FormActions


class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        required = True,
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput
    )
    remember = forms.BooleanField(label='Recuérdame')

    text = forms.TextInput()
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'col s12 m6 l6'
    helper.layout = Layout(
        Div(
            HTML('<i class="material-icons prefix">account_circle</i>'),
            Field('username', css_class='validate'),
            css_class='input-field'
        ),
        Div(
            HTML('<i class="material-icons prefix">lock</i>'),
            Field('password', css_class='validate'),
            css_class='input-field'
        ),
        FormActions(Submit('login', 'Entrar', css_class='btn waves-effect')),
        'remember'
    )
    # helper.add_input(Submit('login', 'Entrar', css_class='btn btn-primary waves-effect'))
