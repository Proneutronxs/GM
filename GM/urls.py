"""GM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,  include
from Apps.Main import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Apps.Main.urls')),

    path('accounts/login/', views.LogIn, name="inicio_sesion"),

    path('accounts/login/GM/', views.custom_login, name='login_gm'),

    path('logout/', logout_then_login, name='logout'),

    path('accounts/login/logout/', logout_then_login, name='log_out'),

]
