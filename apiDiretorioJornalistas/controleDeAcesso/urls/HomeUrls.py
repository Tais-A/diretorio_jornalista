from django.urls import path
from controleDeAcesso.views.HomeView import home_view

urlpatterns = [
    path("", home_view),
]