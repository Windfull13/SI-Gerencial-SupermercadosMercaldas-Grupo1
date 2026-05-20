# Matriz de Trazabilidad

| ID Req. | Requisito | Mockup | Tabla BD | Diagrama UML | Código / Ruta | Estado |
|---------|-----------|--------|----------|--------------|---------------|--------|
| RF-01 | Login de usuarios | [Login](../mockups/Captura%20de%20pantalla%202026-05-11%20131102.png) | `auth_user` | [Casos de uso](diagrams/Diagrama%20de%20casos%20de%20uso.jpeg) | `backend/usuarios/views.py::login_view` | OK |
| RF-02 | Registrar producto | [Gestión de productos](../mockups/Captura%20de%20pantalla%202026-05-11%20131159.png) | `inventario_producto` | [Clases](diagrams/Diagrama%20de%20clases.png) | `backend/inventario/views.py::producto_crear` | OK |
| RF-03 | Consultar inventario en tiempo real | [Dashboard](../mockups/Captura%20de%20pantalla%202026-05-11%20131144.png) | `inventario_producto`, `inventario_movimientoinventario` | [Casos de uso](diagrams/Diagrama%20de%20casos%20de%20uso.jpeg) | `backend/inventario/views.py::dashboard`, `::producto_lista`, `::producto_detalle` | OK |
| RF-04 | Actualizar stock automáticamente | [Control de inventario](../mockups/Captura%20de%20pantalla%202026-05-11%20131218.png) | `inventario_movimientoinventario`, `inventario_producto` | [Secuencia](diagrams/Diagrama%20de%20secuencia.png) | `backend/inventario/views.py::registrar_entrada`, `::registrar_salida` | OK |
| RF-05 | Generar alerta de inventario bajo | [Dashboard](../mockups/Captura%20de%20pantalla%202026-05-11%20131144.png) | `inventario_alertastock` | [Secuencia](diagrams/Diagrama%20de%20secuencia.png) | `backend/inventario/views.py::registrar_salida`, `::alertas_lista`, `::atender_alerta` | OK |
| RF-06 | Generar reportes | [Reportes e informes](../mockups/Captura%20de%20pantalla%202026-05-11%20131334.png) | Consultas sobre `inventario_producto`, `inventario_movimientoinventario`, `inventario_ordencompra` | [Casos de uso](diagrams/Diagrama%20de%20casos%20de%20uso.jpeg) | `backend/inventario/views.py::reportes` | OK |
| RF-07 | Gestionar proveedores | [Gestión de proveedores](../mockups/Captura%20de%20pantalla%202026-05-11%20131243.png) | `inventario_proveedor` | [Clases](diagrams/Diagrama%20de%20clases.png) | `backend/proveedores/views.py::proveedor_lista`, `::proveedor_crear`, `::proveedor_editar`, `::proveedor_desactivar` | OK |
| RF-08 | Generar sugerencia de pedido a proveedor | [Dashboard](../mockups/Captura%20de%20pantalla%202026-05-11%20131144.png) | `inventario_ordencompra`, `inventario_alertastock` | [Secuencia](diagrams/Diagrama%20de%20secuencia.png) | `backend/inventario/views.py::registrar_salida` | OK |

## Cobertura resumida

- La mayoría de requisitos funcionales del SRS ya tienen pantalla, modelo de datos, UML y ruta de código asociada.
- Los reportes ya están implementados en el sistema y también están documentados en `reports/`.
- Esta matriz puede ampliarse con referencias más finas por campo o por caso de uso si el docente solicita mayor detalle.
