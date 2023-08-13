from django.urls import path
from . import views

urlpatterns=[
    path("",views.welcome),
    path("contact/",views.contact),
    path("login/",views.login),
    path("register/",views.register)
]