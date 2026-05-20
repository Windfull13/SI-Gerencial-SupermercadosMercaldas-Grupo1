# Reportes — consultas de ejemplo

1) Órdenes por proveedor (conteo de órdenes):

```sql
SELECT pr.nombre AS proveedor, COUNT(oc.id) AS total_ordenes
FROM inventario_ordencompra oc
JOIN inventario_proveedor pr ON oc.proveedor_id = pr.id
GROUP BY pr.nombre
ORDER BY total_ordenes DESC;
```

2) Ingresos estimados por período (sum(cantidad * precio)):

```sql
SELECT DATE_TRUNC('month', oc.fecha) AS mes,
       SUM(oc.cantidad_sugerida * p.precio) AS ingresos_estimados
FROM inventario_ordencompra oc
JOIN inventario_producto p ON oc.producto_id = p.id
GROUP BY mes
ORDER BY mes DESC;
```

Nota: adapte nombres de tablas si Django usa un prefijo distinto.
