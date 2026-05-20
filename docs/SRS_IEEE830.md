# SIGIM – SRS IEEE 830

**Sistema de Gestión de Inventarios Mercaldas**

## 1. Introducción

Este documento especifica los requerimientos del sistema SIGIM para el supermercado Mercaldas. Su propósito es servir como base para diseño, desarrollo, validación y mantenimiento.

### 1.1 Propósito
El documento está dirigido al equipo de desarrollo, al docente evaluador y a los usuarios del sistema.

### 1.2 Alcance
SIGIM es una aplicación web para registrar productos, controlar inventario, generar alertas de stock bajo, registrar entradas y salidas, y producir reportes de inventario y movimientos.

### 1.3 Stakeholders
| Nombre | Rol | Relación con el sistema |
|---|---|---|
| Administrador del supermercado | Gerente | Supervisión y toma de decisiones |
| Encargado de inventario | Usuario operativo | Control y actualización del inventario |
| Cajero | Usuario operativo | Registra ventas que afectan inventario |
| Proveedor | Actor externo | Suministra productos |

### 1.4 Definiciones
| Término | Definición |
|---|---|
| SRS | Software Requirements Specification |
| RF | Requerimiento Funcional |
| RNF | Requerimiento No Funcional |
| Stakeholder | Interesado en el sistema |

## 2. Descripción general

### 2.1 Perspectiva del producto
SIGIM es un sistema web independiente que se integra funcionalmente con el proceso de ventas para mantener actualizado el inventario.

### 2.2 Funcionalidades principales
- Gestión de productos.
- Control de inventario en tiempo real.
- Registro de entradas y salidas.
- Alertas por niveles bajos de stock.
- Reportes de inventario y movimientos.

### 2.3 Usuarios
| Usuario | Descripción | Experiencia | Frecuencia |
|---|---|---|---|
| Administrador | Supervisa el inventario y reportes | Media | Diaria |
| Encargado de inventario | Registra y controla stock | Media | Diaria |
| Cajero | Consulta disponibilidad y registra ventas | Baja | Diaria |

### 2.4 Restricciones
- Aplicación web.
- Base de datos PostgreSQL.
- Compatibilidad con navegadores modernos.
- Desarrollo dentro del calendario académico.

## 3. Requisitos funcionales resumidos
| ID | Requisito |
|---|---|
| RF-01 | Registrar producto |
| RF-02 | Actualizar stock automáticamente |
| RF-03 | Consultar inventario en tiempo real |
| RF-04 | Generar alerta de inventario bajo |
| RF-05 | Registrar entrada de inventario |
| RF-06 | Generar reportes |
| RF-07 | Gestionar proveedores |
| RF-08 | Generar sugerencia de pedido a proveedor |

## 4. Trazabilidad
La trazabilidad debe seguir la cadena: requisito → mockup → modelo de datos → UML → código → funcionalidad real.

## 5. Observaciones finales
Este archivo resume el contenido del SRS adjunto para dejarlo versionado dentro del repositorio.
