from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, FormView

from .forms import LoginForm


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                message = 'el usuario es valido'
                login(request=self.request, user=user)
            else:
                message = 'El usuario ha sido baneado, por favor contacte con el administrador'
        else:
            message = 'El usuario y/o la contraseña son incorrectos'
        return super(LoginView, self).form_valid(form)


class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'


class AboutView(TemplateView):
    template_name = 'account/about.html'


class TermsView(TemplateView):
    template_name = 'account/terms.html'


class PrivacyView(TemplateView):
    template_name = 'account/privacy.html'
