from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='intenciones_index'),
]
