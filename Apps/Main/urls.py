from django.urls import path
from Apps.Main import views

urlpatterns = [

    path('login/', views.LogIn, name="login_gm"),

    path('', views.GM, name="inicio_gm"),

    path('ver-crc/', views.verPlus, name="ver_plus"),

    path('ver-crc/data-inicial/', views.dataInicialPlus, name="ver_plus_data_inicial"),

    path('ver-crc/data-especifica/', views.dataSubItems, name="ver_plus_data_especifica"),

    path('ver-crc/data-busqueda/', views.busquedaData, name="ver_plus_data_especifica"),

]   