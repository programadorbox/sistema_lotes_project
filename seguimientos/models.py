from django.db import models
from django.conf import settings
from intenciones.models import Intencion

class Seguimiento(models.Model):
    intencion = models.ForeignKey(Intencion, on_delete=models.CASCADE, related_name='seguimientos')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='seguimientos_realizados'
    )

    def __str__(self):
        return f"Seguimiento {self.id} - {self.intencion}"
