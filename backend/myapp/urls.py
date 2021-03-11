from django.urls import include, path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('index',views.index,name='index'),
    #path("register/", views.register_request, name="register"),
]