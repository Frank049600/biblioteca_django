from django.contrib import admin
from django.urls import path, include
from almacen.views import index_acervo as acervo
from almacen.views import acervo_registro, delete_acervo
from inicio.views import index_inicio as inicio
from estadias.views import index_proyectos as proyectos
from django.contrib.auth.decorators import login_required
from login.views import Login, logoutUser
from estadias.views import vistaalumnos as alumnos
from estadias.views import estadias_registro, my_view
from estadias.views import view_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervo/', login_required(acervo), name = 'acervo'),
    path('', login_required(inicio), name = 'inicio'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/', login_required(logoutUser), name = 'logout'),
    path('proyectos/',login_required(proyectos),name='proyectos'),
    path('alumnos/',login_required(alumnos),name='alumnos'),
    # Rutas de registro Acervo
    path('acervo_registro/', login_required(acervo_registro), name='acervo_registro'),
    path('delete_acervo/<colocacion>', login_required(delete_acervo), name='delete_acervo'),
    # path('deleteAcervo/<codigo>', deleteAcervo)

    path('estadias_registro/',login_required(estadias_registro)),
    path('detail/<reporte>',my_view,name='detail_view'),

    path('view_report/', login_required(view_report), name='view_report'),

    # aplicación de sesión
    path('session-security/', include('session_security.urls')),
]
