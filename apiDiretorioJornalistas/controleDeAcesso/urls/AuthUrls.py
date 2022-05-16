from django.urls import path
from controleDeAcesso.views.AuthView import login_view, logout_view, register_view,logout

urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
    path("logout", logout_view, name='logout' )

]
