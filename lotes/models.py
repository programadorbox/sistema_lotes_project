# lotes/models.py
from django.db import models
from django.utils import timezone

class Proyecto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Lote(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = "disponible","Disponible"
        RESERVADO  = "reservado","Reservado"
        VENDIDO    = "vendido","Vendido"
        MORA       = "mora","En mora"
        LIBERADO   = "liberado","Liberado"

    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT, related_name="lotes")
    codigo = models.CharField(max_length=50)  # ej: MzB-L14
    numero = models.CharField(max_length=20)  # o int
    superficie_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_base = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.DISPONIBLE)
    ubicacion_textual = models.CharField(max_length=255, blank=True)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("proyecto","codigo")]
        ordering = ["proyecto","codigo"]

    def __str__(self):
        return f"{self.proyecto} - {self.codigo} ({self.estado})"
