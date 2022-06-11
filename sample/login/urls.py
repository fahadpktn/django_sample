
from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.index,name="templates/index"),
    path("register",views.register,name="templates/register"),
    path("login_user",views.login_user,name="templates/login_user"),
]


