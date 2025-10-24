# lotes/urls_api.py
from django.urls import path
from rest_framework import generics, permissions
from .models import Lote
from .serializers import LoteSerializer

class LoteListAPI(generics.ListAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    permission_classes = [permissions.IsAuthenticated]

urlpatterns = [
    path("lotes/", LoteListAPI.as_view(), name="api_lotes"),
]
