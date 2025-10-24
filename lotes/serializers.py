from rest_framework import serializers
from .models import Lote

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ["id","proyecto","codigo","numero","superficie_m2","precio_base","estado","ubicacion_textual","creado","actualizado"]
