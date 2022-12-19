from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from AppDiretorioJornalistas.views.HomeView import home_view, list_jornalistas_view
from AppDiretorioJornalistas.views.AuthViews import login_view, logout_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view), #Busca de joranlistas e Glossario
    path('',  list_jornalistas_view, name='jornalistas'),

    path("login", login_view, name='login'), #username e senha
    path("register", register_view, name='register'), # username associação e senha
    path("logout", logout_view, name='logout' ), #redireciona para home 


    # path('jornalista/<int:id>', jornalista_view, name='jornalista'), #resumo do jornalista


    # path('usuario/<int:id>', usuario_view), cadastro com informações gerais
    # path('usuario/obra/<int:id>/'), cadastro de obra
    # path('usuario/historico/<int:id>'), #cadastro de historico 

    # path('revisor/<int:id>') listas de jornalistas da associaçao 
    # caminho para ver o resumo de jornalista, validar obra e validar historico etc 
    #path ('editar', editar_usuario, name='editar-usuario')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
