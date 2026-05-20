# Informe de inventario general

**Sistema:** SIGIM - Sistema de Gestión de Inventarios Mercaldas  
**Fecha del corte:** 2026-05-20  
**Fuente:** Base de datos PostgreSQL `sigim_db`

## Resumen ejecutivo

El inventario actual muestra una base de datos funcional con productos clasificados por estado de stock. En el corte consultado hay 15 productos activos, 5 proveedores, 7 movimientos registrados y 1 orden de compra sugerida. El 26.7% del inventario está en estado de bajo stock o sin stock, lo que justifica el seguimiento de alertas y reposiciones.

## Indicadores clave

| Indicador | Valor |
| - | -: |
| Proveedores registrados | 5 |
| Productos registrados | 15 |
| Productos en stock normal | 10 |
| Productos con bajo stock | 4 |
| Productos sin stock | 1 |
| Movimientos registrados | 7 |
| Alertas registradas | 1 |
| Órdenes de compra | 1 |

## Productos críticos

| Código | Producto | Disponible | Stock mínimo | Proveedor |
| - | - | -: | -: | - |
| ALI-003 | Aceite Gourmet 1L | 0 | 15 | Distribuidora Alimentaria del Eje |
| ASE-003 | Shampoo HyS 400ml | 3 | 10 | Aseo y Hogar Ltda. |
| LAC-003 | Queso Campesino 250g | 5 | 10 | Lacteos del Cafe SA |
| ALI-002 | Frijol Baltico 500g | 8 | 20 | Distribuidora Nacional de Granos |
| LAC-001 | Leche Colanta 1L | 12 | 30 | Lacteos del Cafe SA |

## Observaciones

- El producto con mayor criticidad en el corte es `ALI-003 - Aceite Gourmet 1L`, que quedó en cero unidades.
- Existe una orden de compra sugerida para reabastecimiento automático.
- El inventario sigue mostrando rotación activa con entradas y salidas recientes.

## Consulta SQL de apoyo

```sql
SELECT
    p.codigo_unico,
    p.nombre,
    p.cantidad_disponible,
    p.stock_minimo,
    pr.nombre AS proveedor
FROM inventario_producto p
LEFT JOIN inventario_proveedor pr ON pr.id = p.proveedor_id
WHERE p.activo = TRUE
ORDER BY p.cantidad_disponible ASC;
```

```sql
SELECT
    CASE
        WHEN cantidad_disponible = 0 THEN 'sin_stock'
        WHEN cantidad_disponible <= stock_minimo THEN 'bajo_stock'
        ELSE 'normal'
    END AS estado,
    COUNT(*) AS total
FROM inventario_producto
WHERE activo = TRUE
GROUP BY 1;
```