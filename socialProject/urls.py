from django.conf.urls import include, url
from django.contrib import admin

from account.views import LoginView, AboutView, TermsView, PrivacyView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^terms/$', TermsView.as_view(), name='terms'),
    url(r'^privacy/$', PrivacyView.as_view(), name='privacy'),
    url(r'^', include('account.urls', namespace='account'))
]
