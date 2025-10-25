# 🧩 Sistema de Roles y Permisos — Proyecto **Sistema Lotes**

Este documento define la estructura de **roles, permisos y flujo de trabajo** implementada en el sistema Django **Sistema Lotes**.  
Todos los roles y permisos se configuran directamente desde el **panel de administración de Django**, sin necesidad de modificar el código.

---

## ⚙️ Roles definidos

### 🧑‍💼 Superusuario
- Tiene **control total** del sistema.
- Puede crear, editar y eliminar cualquier registro.
- Tiene acceso completo al panel `/admin/`.

**Permisos automáticos:**
> Todos los disponibles (Django otorga permisos totales a `is_superuser=True`).

---

### 🧑‍🏫 Administrador
- Su función es de **consulta y supervisión**.
- No puede crear, editar ni eliminar registros.
- Solo puede **ver** la información de lotes, intenciones (ventas), clientes y seguimientos.

**Permisos asignados:**

| App | Modelo | Permisos activos |
|------|---------|------------------|
| clientes | cliente | ✅ Can view cliente |
| intenciones | intencion | ✅ Can view intencion |
| lotes | lote | ✅ Can view lote |
| lotes | proyecto | ✅ Can view proyecto |
| seguimientos | seguimiento | ✅ Can view seguimiento |

**Restricciones:**
- ❌ No puede crear (`add`)
- ❌ No puede editar (`change`)
- ❌ No puede eliminar (`delete`)

---

### 🧑‍🔧 Vendedor (Usuario común)
- Representa a los vendedores o agentes comerciales.
- Puede registrar nuevos clientes y crear intenciones (ventas).
- Puede ver todas las intenciones (para fomentar la competencia).
- No puede modificar ni eliminar datos ajenos.

**Permisos asignados:**

| App | Modelo | Permisos activos |
|------|---------|------------------|
| clientes | cliente | ✅ Can add cliente, ✅ Can view cliente |
| intenciones | intencion | ✅ Can add intencion, ✅ Can view intencion |
| lotes | lote | ✅ Can view lote |
| lotes | proyecto | ✅ Can view proyecto |

**Restricciones:**
- ❌ No puede editar (`change`)
- ❌ No puede eliminar (`delete`)

---

## 🧱 Estructura de Grupos en Django

Los roles se implementan como **Grupos** dentro del panel de administración de Django.

### Pasos para crear grupos:

1. Entra al panel `/admin/auth/group/`
2. Crea los siguientes grupos:
   - `Administradores`
   - `Vendedores`
3. Asigna los permisos descritos en las tablas anteriores.
4. Guarda los cambios.

---

## 👤 Asignación de roles a usuarios

1. Ve a `/admin/auth/user/`
2. Selecciona un usuario existente o crea uno nuevo.
3. En el campo **Grupos**, asigna:
   - `Administradores` o `Vendedores`
4. Guarda los cambios.

> 🟢 El superusuario no necesita grupo (ya tiene todos los permisos).

---

## 🔁 Flujo de trabajo real

| Acción | Realizada por | Descripción |
|---------|----------------|--------------|
| Crear cliente | 🧑‍🔧 Vendedor | Registra un nuevo interesado. |
| Crear intención (venta) | 🧑‍🔧 Vendedor | Asocia el cliente con un lote. |
| Ver intenciones | Todos | Fomenta la competencia entre vendedores. |
| Revisar datos o eliminar registros | 🧑‍💼 Superusuario | Control total del sistema. |

---

## 💡 Bonus: Asociación automática de clientes al vendedor

> (Opcional — implementar en `clientes/models.py`)

Para registrar automáticamente **qué vendedor creó cada cliente**, se puede agregar este método en el modelo `Cliente`:

```python
def save(self, *args, **kwargs):
    if not self.pk and not self.creado_por_id:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        # Asociar automáticamente el usuario logueado (si existe en request)
        # Este método se complementa desde la vista o el admin
    super().save(*args, **kwargs)

Administ 	Gestor	    123!4567
Vendedor 	vende1	    123!4567	
Vendedor 	vende2	    123!4567	
Vendedor 	vende3	    123!4567