
from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.index,name="templates/index"),
    path("login",views.login_user,name="templates/login"),
    path("register",views.register,name="templates/register")
]


