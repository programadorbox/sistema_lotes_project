from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("interesado", "Interesado"),
            ("visito", "Visitó"),
            ("reservo", "Reservó"),
            ("compro", "Compró"),
            ("desistio", "Desistió"),
            ("mora", "En mora"),
        ],
        default="interesado"
    )
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
