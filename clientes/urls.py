from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),   # Página principal de clientes
    path('nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
]
