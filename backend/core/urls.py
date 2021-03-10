from django.urls import path
from . import views
# from . import HodViews

urlpatterns = [
  path('', views.ShowLoginPage, name="login"),
  path('doLogin', views.doLogin),
   path('add_employer', views.add_employer),
  path('add_employer_save', views.add_employer_save),
  path('admin_home', views.admin_home),
]