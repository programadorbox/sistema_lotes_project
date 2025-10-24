# lotes/views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from .models import Lote

@login_required
@permission_required("lotes.view_lote", raise_exception=True)
def lista_lotes(request):
    estado = request.GET.get("estado")
    qs = Lote.objects.select_related("proyecto").all()
    if estado:
        qs = qs.filter(estado=estado)
    return render(request, "lotes/lista.html", {"lotes": qs})

