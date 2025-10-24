# clientes/admin.py
from django.contrib import admin
from .models import Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","telefono","email","estado","creado")
    list_filter = ("estado",)
    search_fields = ("nombre","email","telefono")
