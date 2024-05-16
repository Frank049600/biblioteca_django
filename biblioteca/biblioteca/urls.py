from django.contrib import admin
from django.urls import path
from almacen.views import index_acervo as acervo
from inicio.views import index_inicio as inicio
from estadias.views import index_proyectos as proyectos
from django.contrib.auth.decorators import login_required
from login.views import Login, logoutUser
from estadias.views import vistaalumnos as alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervo/', login_required(acervo), name = 'acervo'),
    path('', login_required(inicio), name = 'inicio'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/', login_required(logoutUser), name = 'logout'),
    path('proyectos/',login_required(proyectos),name='proyectos'),
    path('alumnos/',login_required(alumnos),name='alumnos'),

]
