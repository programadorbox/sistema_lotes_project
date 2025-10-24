from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo temporal
    path('', views.index, name='clientes_index'),
]
