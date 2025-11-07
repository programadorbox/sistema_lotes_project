# Sistema de Roles y Permisos — Proyecto **Sistema Lotes**

Este documento define la estructura de **roles, permisos y flujo de trabajo** implementada en el sistema Django **Sistema Lotes**.  
Todos los roles y permisos se configuran directamente desde el **panel de administración de Django**, sin necesidad de modificar el código.

---

##  Roles definidos

###  Superusuario
- Tiene **control total** del sistema.
- Puede crear, editar y eliminar cualquier registro.
- Tiene acceso completo al panel `/admin/`.



### Administrador
- Su nción es de **consulta y supervisión**.
- No puede crear, editar ni eliminar registros.
- Solo puede **ver** la información de lotes, intenciones (ventas), clientes y seguimientos.

**Permisos asignados:**

| App | Modelo | Permisos activos |
|------|---------|------------------|
| clientes | cliente | Can view cliente |
| intenciones | intencion |  Can view intencion |
| lotes | lote | Can view lote |
| lotes | proyecto | Can view proyecto |
| seguimientos | seguimiento | Can view seguimiento |


---

###  Vendedor (Usuario común)
- Representa a los vendedores o agentes comerciales.
- Puede registrar nuevos clientes y crear intenciones (ventas).
- Puede ver todas las intenciones (para fomentar la competencia).
- No puede modificar ni eliminar datos ajenos.

**Permisos asignados:**

| App | Modelo | Permisos activos |
|------|---------|------------------|
| clientes | cliente |  Can add cliente, Can view cliente |
| intenciones | intencion | Can add intencion,  Can view intencion |
| lotes | lote |  Can view lote |
| lotes | proyecto |  Can view proyecto |

**Restricciones:**
-  No puede editar (`change`)
- No puede eliminar (`delete`)

---

## Estructura de Grupos en Django

Los roles se implementan como **Grupos** dentro del panel de administración de Django.

### Pasos para crear grupos:

1. Entra al panel `/admin/auth/group/`
2. Crea los siguientes grupos:
   - `Administradores`
   - `Vendedores`
3. Asigna los permisos descritos en las tablas anteriores.
4. Guarda los cambios.

---


## Flujo de trabajo real

| Acción | Realizada por | Descripción |
|---------|----------------|--------------|
| Crear cliente | 🧑‍🔧 Vendedor | Registra un nuevo interesado. |
| Crear intención (venta) | 🧑‍🔧 Vendedor | Asocia el cliente con un lote. |
| Ver intenciones | Todos | Fomenta la competencia entre vendedores. |
| Revisar datos o eliminar registros | 🧑‍💼 Superusuario | Control total del sistema. |

---

    
    credenciales, se que es una pesima practica esto, pero es solo a modo de prueba 

Administ 	Gestor	    123!4567
Vendedor 	vende1	    123!4567	
Vendedor 	vende2	    123!4567	
Vendedor 	vende3	    123!4567