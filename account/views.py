from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import TemplateView, FormView, RedirectView
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.forms import LoginForm


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    # form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        self.success_url = self.request.GET.get('next','')
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = authenticate(username=form.get_user(), password=form.get_password())
        if user is not None:
            if not user.is_active:
                form.errors['inactive'] = _('El usuario ha sido baneado')
                return self.form_invalid(form)

            login(self.request, user)
            return super(LoginView, self).form_valid(form)

        else:
            form.errors['incorrect'] = _('Usuario o contraseña incorrecto')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    template_name = 'account/about.html'


class TermsView(TemplateView):
    template_name = 'account/terms.html'


class PrivacyView(TemplateView):
    template_name = 'account/privacy.html'
