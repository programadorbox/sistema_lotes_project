# usuarios/management/commands/seed_roles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Crea grupos: Administrador, Supervisor, Vendedor"

    def handle(self, *args, **kwargs):
        admin_group, _ = Group.objects.get_or_create(name="Administrador")
        supervisor_group, _ = Group.objects.get_or_create(name="Supervisor")
        vendedor_group, _ = Group.objects.get_or_create(name="Vendedor")

        # Permisos base
        all_perms = Permission.objects.all()

        # Admin: todos los permisos
        admin_group.permissions.set(all_perms)

        # Supervisor: solo ver (view_) en todas las apps
        supervisor_perms = [p for p in all_perms if p.codename.startswith("view_")]
        supervisor_group.permissions.set(supervisor_perms)

        # Vendedor: puede ver y agregar clientes e intenciones, pero NO borrar lotes
        vendedor_perms = [p for p in all_perms if p.codename.startswith("view_")]
        vendedor_perms += [p for p in all_perms if p.codename.startswith("add_") and ("cliente" in p.codename or "intencion" in p.codename)]
        vendedor_perms += [p for p in all_perms if p.codename.startswith("change_") and ("cliente" in p.codename or "intencion" in p.codename)]
        vendedor_group.permissions.set(vendedor_perms)

        self.stdout.write(self.style.SUCCESS("Grupos y permisos configurados."))
