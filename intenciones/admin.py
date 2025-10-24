# intenciones/admin.py
from django.contrib import admin
from .models import Intencion
@admin.register(Intencion)
class IntencionAdmin(admin.ModelAdmin):
    list_display = ("lote","vendedor","cliente","estado","activa","creado")
    list_filter = ("estado","activa","vendedor","lote__proyecto")
    search_fields = ("lote__codigo","cliente__nombre","vendedor__username")
