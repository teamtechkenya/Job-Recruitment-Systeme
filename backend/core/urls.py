from django.urls import path
from . import views
from . import HodViews

urlpatterns = [
  path('', views.ShowLoginPage, name="login"),
  path('doLogin', views.doLogin),
]