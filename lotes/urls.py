from django.urls import path
from .views import lista_lotes

urlpatterns = [
    path("", lista_lotes, name="lotes_lista"),
]
