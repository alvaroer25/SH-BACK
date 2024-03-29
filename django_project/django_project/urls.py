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
from django.conf.urls import url
from core import views

urlpatterns = [
    url('', views.img_enf, name="img_enf"),
    url('about/', views.about, name="about"),
    url(r'^busqueda_enf/(?P<cod_enf>[0-9]+)$',views.Busqueda_img_prueba, name="Busqueda_img_prueba"),
    url('admin/', admin.site.urls),
    url(r'^busqueda_x_letra/(?P<p_enfermedad>)$',views.Busqueda_por_letra, name="Busqueda_por_letra")
]
