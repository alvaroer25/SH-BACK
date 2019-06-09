"""Pdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from core import views

urlpatterns = [
    path('', views.enf_imagen, name="enf_imagen"),
    path('about/', views.about, name="about"),
    re_path(r'^busqueda_enf/(?P<cod_enf>[0-9]+)$',views.Busqueda_img_prueba, name="Busqueda_img_prueba"),
    path('admin/', admin.site.urls),
    re_path(r'^busqueda_x_letra/(?P<p_enfermedad>)$',views.Busqueda_por_letra, name="Busqueda_por_letra")
]
