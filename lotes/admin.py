# lotes/admin.py
from django.contrib import admin
from .models import Proyecto, Lote
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre","activo","creado")
    list_filter = ("activo",)

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ("proyecto","codigo","numero","estado","superficie_m2","precio_base")
    list_filter = ("proyecto","estado")
    search_fields = ("codigo","numero","ubicacion_textual")
