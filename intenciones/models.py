# intenciones/models.py
from django.db import models, transaction
from django.conf import settings
from django.utils import timezone
from lotes.models import Lote


class Intencion(models.Model):
    class Estado(models.TextChoices):
        INTERES = "interes", "Interés"
        RESERVA = "reserva", "Reserva"
        CONFIRMADA = "confirmada", "Venta confirmada"
        CANCELADA = "cancelada", "Cancelada"

    lote = models.ForeignKey(
        Lote,
        on_delete=models.PROTECT,
        related_name="intenciones"
    )
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.PROTECT,
        related_name="intenciones"
    )
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.INTERES
    )
    nota = models.TextField(blank=True)
    creado = models.DateTimeField(default=timezone.now)  # 👈 Este reemplaza 'fecha'
    actualizado = models.DateTimeField(auto_now=True)
    activa = models.BooleanField(default=True)  # solo una activa por lote

    class Meta:
        constraints = [
            # Garantiza UNA intención activa por lote
            models.UniqueConstraint(
                fields=["lote"],
                condition=models.Q(activa=True),
                name="uniq_intencion_activa_por_lote"
            )
        ]
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.lote.codigo} - {self.vendedor.username} - {self.estado}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            # Regla de negocio: estados afectan el Lote
            if self.estado == self.Estado.RESERVA:
                if self.lote.estado != Lote.Estado.DISPONIBLE:
                    raise ValueError("El lote no está disponible para reservar.")
                self.lote.estado = Lote.Estado.RESERVADO
                self.lote.save(update_fields=["estado", "actualizado"])

            elif self.estado == self.Estado.CONFIRMADA:
                self.lote.estado = Lote.Estado.VENDIDO
                self.lote.save(update_fields=["estado", "actualizado"])
                # al confirmar la venta, esta intención queda activa=False
                self.activa = False

            elif self.estado == self.Estado.CANCELADA:
                # liberar el lote
                if self.lote.estado in (Lote.Estado.RESERVADO, Lote.Estado.MORA):
                    self.lote.estado = Lote.Estado.LIBERADO
                    self.lote.save(update_fields=["estado", "actualizado"])
                self.activa = False

            super().save(*args, **kwargs)
