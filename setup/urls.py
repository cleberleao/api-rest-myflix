"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from myflix.views import  userViewSet, streamViewSet, listaViewSet, listaUser, listaStream
from rest_framework import routers, permissions

router = routers.DefaultRouter()
router.register('users', userViewSet, basename='users')
router.register('streams', streamViewSet, basename='streams')
router.register('listas',listaViewSet, basename='listas')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentação",
        default_version='v1',
        description="Documentação da API para o seu projeto Django",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="seuemail@dominio.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:pk>/listas/', listaUser.as_view()),
    path('streams/<int:pk>/listas/', listaStream.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
