from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Intencion

@admin.register(Intencion)
class IntencionAdmin(admin.ModelAdmin):
    list_display = ("cliente", "vendedor", "lote", "colored_estado", "creado")
    list_filter = ("estado", "vendedor")
    search_fields = ("cliente__nombre", "lote__codigo")

    def colored_estado(self, obj):
        estilos = {
            "interes": ("#0d6efd", "💬 Interés"),        # Azul Bootstrap
            "reserva": ("#ffc107", "⏳ Reserva"),        # Amarillo
            "confirmada": ("#198754", "✅ Confirmada"),  # Verde Bootstrap
            "cancelada": ("#dc3545", "❌ Cancelada"),    # Rojo
        }
        color, texto = estilos.get(obj.estado, ("gray", obj.get_estado_display()))
        html = f'<span style="display:inline-block;background-color:{color} !important;color:white !important;padding:4px 10px;border-radius:10px;font-weight:bold;font-size:13px;min-width:90px;text-align:center;">{texto}</span>'
        
        return mark_safe(html)

    colored_estado.allow_tags = True
    colored_estado.short_description = "Estado"
    colored_estado.admin_order_field = "estado"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name="Administradores").exists():
            return True
        if obj is not None and obj.vendedor == request.user:
            return True
        return False
