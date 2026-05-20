# Informe de movimientos recientes

**Sistema:** SIGIM - Sistema de Gestión de Inventarios Mercaldas  
**Fecha del corte:** 2026-05-20  
**Fuente:** Base de datos PostgreSQL `sigim_db`

## Resumen ejecutivo

En el corte actual existen 7 movimientos registrados en el inventario. La mayor parte de la actividad reciente corresponde a salidas operativas y entradas de ajuste para reabastecimiento. Este reporte sirve para auditar la trazabilidad entre los movimientos y el cambio real de existencias.

## Movimientos más recientes

| Fecha | Tipo | Producto | Cantidad | Usuario | Proveedor | Descripción |
| - | - | - | -: | - | - | - |
| 2026-05-20 14:43 | SALIDA | Aceite Gourmet 1L | 45 | admin | La cocina |  |
| 2026-05-20 14:42 | ENTRADA | Azucar Riopaila 2kg | 50 | admin | Distribuidora Alimentaria del Eje |  |
| 2026-05-20 14:22 | SALIDA | Agua Cristal 600ml | 15 | admin | Distribuidora Alimentaria del Eje |  |
| 2026-05-20 14:22 | SALIDA | Agua Cristal 600ml | 15 | admin | Distribuidora Alimentaria del Eje | 1 |
| 2026-05-20 14:21 | ENTRADA | Criolla burgers | 15 | admin | La cocina | Entraron 15 burgers |
| 2026-05-20 13:20 | SALIDA | Agua Cristal 600ml | 1 | admin | Distribuidora Alimentaria del Eje |  |
| 2026-05-19 15:53 | ENTRADA | Criolla burgers | 3 | admin | La cocina | El dia 19/05/206 ingresaron 3 unidades frescas de Criolla burgers |

## Lectura operativa

- El sistema está registrando movimientos tanto automáticos como manuales.
- Se observa trazabilidad por usuario responsable en todos los eventos recuperados.
- El historial reciente muestra productos con alta rotación y entradas puntuales para reposición.

## Consulta SQL de apoyo

```sql
SELECT
    m.fecha,
    m.tipo,
    p.codigo_unico,
    p.nombre,
    m.cantidad,
    u.username AS usuario,
    pr.nombre AS proveedor,
    m.descripcion
FROM inventario_movimientoinventario m
JOIN inventario_producto p ON p.id = m.producto_id
LEFT JOIN auth_user u ON u.id = m.usuario_responsable_id
LEFT JOIN inventario_proveedor pr ON pr.id = m.proveedor_id
ORDER BY m.fecha DESC;
```

```sql
SELECT
    tipo,
    COUNT(*) AS total_movimientos,
    SUM(cantidad) AS unidades_movidas
FROM inventario_movimientoinventario
GROUP BY tipo
ORDER BY tipo;
```