# clientes/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Cliente


# --- Verificar si el usuario pertenece al grupo 'Vendedores' ---
def es_vendedor(user):
    return user.groups.filter(name='Vendedores').exists() or user.is_superuser


# --- Vista para crear cliente ---
@login_required
@user_passes_test(es_vendedor)
def nuevo_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        estado = request.POST.get('estado', 'interesado')

        Cliente.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email,
            estado=estado
        )

        # ✅ Mensaje de confirmación
        messages.success(request, "✅ Cliente creado correctamente")
        return redirect('/clientes/')

    return render(request, 'clientes/nuevo_cliente.html')


# --- Vista para listar clientes ---
@login_required
@user_passes_test(es_vendedor)
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-creado')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})
