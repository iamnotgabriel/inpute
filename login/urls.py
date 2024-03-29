"""inpute URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from login.views import (
    cadastro,
    home,
    ProfileView,
    profile_update,
    custom_login,
    my_profile,
    change_password,
    
    )

urlpatterns = [
    path('', include('django.contrib.auth.urls') ),

    path('', custom_login ),

    path('cadastro/', cadastro, name= 'cadastro'),

    path('perfil/<int:pk>', ProfileView.as_view(
        template_name = 'login/profile_detail.html'), name= 'perfil' ),

    path('perfil/edit', profile_update, name= 'perfil_edit'),

    path('perfil/my', my_profile, name= 'my_profile'),

    path('perfil/senha', change_password, name = 'change_password' )

]
