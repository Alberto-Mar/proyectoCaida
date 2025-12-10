"""
URL configuration for laCaida project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from common import views as v_common
from eventos import views as v_eventos
from users import views as v_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_common.LoginView.as_view(), name="login"),
    path('login', v_common.LoginView.as_view(), name="login"),
    path('error/', v_common.ErrorView.as_view(), name="error" ),
    path('inicio_hermano/', v_users.HermanoView.as_view(), name="inicio_hermano" ),
    path('inicio_admin/', v_users.AdminView.as_view(), name="inicio_admin" ),
    path('crear_acto/', v_common.CrearActoView.as_view(), name="crear_acto" ),
    path('crear_hermano_auto/', v_users.UserCreateView.as_view(), name="crear_hermano_auto" ),
    path('lista_hermanos/', v_users.ListaHermanosView.as_view(), name="lista_hermanos" ),
    path('crear_hermano/', v_users.CrearHermanoView.as_view(), name="crear_hermano" ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)