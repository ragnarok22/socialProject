from django.conf.urls import include, url
from django.contrib import admin

from account.views import LoginView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', LoginView.as_view(), name='login'),
]
