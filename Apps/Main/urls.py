from django.urls import path
from Apps.Main import views

urlpatterns = [

    path('login/', views.LogIn, name="login_gm"),

    path('', views.GM, name="inicio_gm"),

    path('ver-plus/', views.verPlus, name="ver_plus"),

]   