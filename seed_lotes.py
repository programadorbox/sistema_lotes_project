import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_lotes.settings')
django.setup()

from lotes.models import Lote, Proyecto

# Asegúrate de que exista al menos un proyecto
proyecto, _ = Proyecto.objects.get_or_create(nombre="Proyecto Central")

estados = ["disponible", "reservado", "vendido", "mora", "liberado"]

# Generar 100 lotes
for i in range(1, 101):
    Lote.objects.create(
        proyecto=proyecto,
        codigo=f"LT-{i:03}",
        numero=i,
        superficie_m2=Decimal(random.uniform(100, 500)).quantize(Decimal('0.01')),
        precio_base=Decimal(random.uniform(20000, 80000)).quantize(Decimal('0.01')),
        estado=random.choice(estados),
        ubicacion_textual=f"Lote número {i} dentro del Proyecto Central",
    )

print("✅ Se crearon 100 lotes correctamente.")

