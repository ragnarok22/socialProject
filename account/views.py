from django.views.generic import TemplateView, FormView

from .forms import LoginForm


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm


class AboutView(TemplateView):
    template_name = 'account/about.html'


class TermsView(TemplateView):
    template_name = 'account/terms.html'


class PrivacyView(TemplateView):
    template_name = 'account/privacy.html'
