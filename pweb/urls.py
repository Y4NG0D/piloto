"""
URL configuration for piloto project.

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
from home import views

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('item/<int:id>/', views.exibir_item, name='item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('diasemana/<int:dia>/', views.diasemana, name='diasemana'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/forms/', views.forms, name='forms')
]   


