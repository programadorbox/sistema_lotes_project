from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Intencion
from clientes.models import Cliente
from lotes.models import Lote


# --- Función para validar acceso ---
def es_vendedor_o_admin(user):
    return (
        user.is_superuser
        or user.groups.filter(name__in=["Vendedores", "Administradores"]).exists()
    )


# --- Vista: registrar nueva intención ---
@login_required
@user_passes_test(es_vendedor_o_admin)
def nueva_intencion(request):
    from django.shortcuts import get_object_or_404

    clientes = Cliente.objects.all().order_by('nombre')
    lotes = Lote.objects.all().order_by('codigo')

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        lote_id = request.POST.get('lote')
        estado = request.POST.get('estado')
        nota = request.POST.get('nota', '')

        # Validar campos obligatorios
        if not cliente_id or not lote_id or not estado:
            messages.error(request, "⚠️ Debes seleccionar cliente, lote y estado.")
            return render(request, 'intenciones/nueva_intencion.html', {
                'clientes': clientes,
                'lotes': lotes,
            })

        try:
            cliente = get_object_or_404(Cliente, id=cliente_id)
            lote = get_object_or_404(Lote, id=lote_id)

            Intencion.objects.create(
                cliente=cliente,
                lote=lote,
                vendedor=request.user,
                estado=estado,
                nota=nota
            )

            messages.success(request, "✅ Intención registrada correctamente.")
            return redirect('/intenciones/lista/')

        except Exception as e:
            messages.error(request, f"❌ Error al guardar: {str(e)}")

    return render(request, 'intenciones/nueva_intencion.html', {
        'clientes': clientes,
        'lotes': lotes,
    })



# --- Vista: listar todas las intenciones (todos los vendedores pueden ver todas) ---
@login_required
@user_passes_test(es_vendedor_o_admin)
def lista_intenciones(request):
    vendedor_filtro = request.GET.get('vendedor')
    estado_filtro = request.GET.get('estado')

    intenciones = Intencion.objects.select_related('cliente', 'lote', 'vendedor').order_by('-creado')

    # Filtrar por vendedor
    if vendedor_filtro:
        intenciones = intenciones.filter(vendedor__username=vendedor_filtro)

    # Filtrar por estado
    if estado_filtro:
        intenciones = intenciones.filter(estado=estado_filtro)

    # Lista de vendedores únicos (para el filtro)
    vendedores = Intencion.objects.values_list('vendedor__username', flat=True).distinct()

    return render(request, 'intenciones/lista_intenciones.html', {
        'intenciones': intenciones,
        'vendedores': vendedores,
    })


# --- Vista index: redirigir a lista ---
@login_required
@user_passes_test(es_vendedor_o_admin)
def index(request):
    return redirect('lista_intenciones')
