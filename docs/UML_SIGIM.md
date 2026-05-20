# SIGIM – Guía UML

## Diagramas requeridos
- Diagrama de casos de uso.
- Diagrama de actividades.
- Diagrama de clases.
- Diagrama de secuencia.

## Casos de uso
Los actores principales son: Administrador, Encargado de Inventario, Cajero y Proveedor.

Casos de uso identificados:
- Autenticarse en el sistema.
- Registrar producto.
- Consultar inventario en tiempo real.
- Actualizar stock automáticamente.
- Generar alerta de inventario bajo.
- Registrar entrada de inventario.
- Generar reportes.
- Gestionar proveedores.
- Generar sugerencia de pedido a proveedor.

## Actividades
El proceso principal cubre el registro de venta, actualización de inventario, validación de stock mínimo, generación de alerta y creación de pedido sugerido.

## Clases
Entidades principales del dominio:
- Usuario.
- Producto.
- Proveedor.
- MovimientoInventario.
- AlertaStock.
- OrdenCompra.

## Secuencia
La secuencia principal modela la actualización automática de stock después de una venta o entrada, y la generación de alerta/pedido cuando el stock cae por debajo del mínimo.

## Observaciones
Este documento deja versionada la guía UML adjunta, mientras los diagramas gráficos se almacenan en `mockups/` o `docs/diagrams/` según el tipo de entregable.
