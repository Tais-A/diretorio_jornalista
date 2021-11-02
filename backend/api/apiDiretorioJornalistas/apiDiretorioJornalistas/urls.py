"""apiDiretorioJornalistas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

from controleDeAcesso.urls import HomeUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('controleDeAcesso.urls.HomeUrls')), #home(contorole de acesso?)
    path('', include('controleDeAcesso.urls.AuthUrls')),
    path('jornalista/', include('controleDeAcesso.urls.JornalistaUrls')),
    path('usuario/', include('controleDeAcesso.urls.UsuarioUrls')),

    path('curriculo/', include('curriculo.urls')),
    path('deontologia/', include('deontologia.urls')),
    path('publicacao/', include('publicacao.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 