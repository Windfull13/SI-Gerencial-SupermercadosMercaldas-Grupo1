# Informe de alertas y órdenes de compra

**Sistema:** SIGIM - Sistema de Gestión de Inventarios Mercaldas  
**Fecha del corte:** 2026-05-20  
**Fuente:** Base de datos PostgreSQL `sigim_db`

## Resumen ejecutivo

El sistema mantiene el control de stock bajo mediante alertas automáticas y sugerencias de orden de compra. En el corte actual existe 1 alerta registrada, ya atendida, y 1 orden de compra en estado sugerido. Esto confirma que el flujo de alerta y sugerencia automática está funcionando.

## Alertas registradas

| Fecha | Estado | Producto | Nivel crítico | Mensaje |
| - | - | - | -: | - |
| 2026-05-20 14:43 | ATENDIDA | Aceite Gourmet 1L | 0 | Stock de "Aceite Gourmet 1L" en nivel crítico: 0 unidades. |

## Órdenes de compra registradas

| Fecha | Estado | Producto | Proveedor | Cantidad sugerida | Observaciones |
| - | - | - | - | -: | - |
| 2026-05-20 14:43 | SUGERIDA | Aceite Gourmet 1L | Distribuidora Alimentaria del Eje | 45 | Generada automáticamente por alerta de stock. |

## Observaciones

- La alerta generada se atendió en el sistema, lo cual evita acumulación de incidencias activas.
- La sugerencia de orden de compra se creó automáticamente con base en el stock crítico.
- El módulo de abastecimiento está enlazado con proveedor, producto y alerta.

## Consulta SQL de apoyo

```sql
SELECT
    a.fecha,
    a.estado,
    p.codigo_unico,
    p.nombre,
    a.nivel_critico,
    a.mensaje
FROM inventario_alertastock a
JOIN inventario_producto p ON p.id = a.producto_id
ORDER BY a.fecha DESC;
```

```sql
SELECT
    o.fecha,
    o.estado,
    p.codigo_unico,
    p.nombre,
    pr.nombre AS proveedor,
    o.cantidad_sugerida,
    o.observaciones
FROM inventario_ordencompra o
JOIN inventario_producto p ON p.id = o.producto_id
JOIN inventario_proveedor pr ON pr.id = o.proveedor_id
ORDER BY o.fecha DESC;
```