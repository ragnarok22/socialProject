from django.conf.urls import include, url
from django.contrib import admin

from account.views import LoginView, AboutView, TermsView, PrivacyView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', LoginView.as_view(), name='login'),
    url(r'^', AboutView.as_view(), name='about'),
    url(r'^', TermsView.as_view(), name='terms'),
    url(r'^', PrivacyView.as_view(), name='privacy'),
]
