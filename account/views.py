from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'account/login.html'


class AboutView(TemplateView):
    template_name = 'account/about.html'


class TermsView(TemplateView):
    template_name = 'account/terms.html'


class PrivacyView(TemplateView):
    template_name = 'account/privacy.html'
