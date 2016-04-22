from django.conf.urls import url

from .views import DashboardView

urlpatterns = [
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard')
]
