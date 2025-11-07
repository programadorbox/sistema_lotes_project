from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='intenciones_index'),
    path('nueva/', views.nueva_intencion, name='nueva_intencion'),
    path('lista/', views.lista_intenciones, name='lista_intenciones'),
]
