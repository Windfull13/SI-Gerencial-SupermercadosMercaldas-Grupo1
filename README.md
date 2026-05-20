# SI-Gerencial-SupermercadosMercaldas-Grupo1

**SIGIM — Sistema de Gestión de Inventarios Mercaldas**

Sistema de información gerencial para el control de inventarios del supermercado Mercaldas, desarrollado como proyecto de aula para la Universidad de Caldas.

**Integrantes:** Ángelo Franco Orozco · Shirley Ximena Ramírez López
**Stack:** Django 4.2 · PostgreSQL · Bootstrap 5

---

## Estructura del repositorio

```text
SI-Gerencial-SupermercadosMercaldas-Grupo1/
├── README.md
├── database/
├── docs/
├── frontend/
│   ├── README.md
│   ├── templates/
│   └── static/
├── mockups/
├── reports/
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── inventario/
    ├── proveedores/
    ├── usuarios/
    ├── sigim/
    └── templates/
```

---

## Estructura funcional

- `backend/`: código Django, modelos, vistas y formularios.
- `database/`: dump PostgreSQL y scripts de carga de datos.
- `frontend/`: plantillas HTML y estáticos del sistema.
- `docs/`: SRS, UML, trazabilidad y manuales.
- `mockups/`: capturas y prototipos aprobados.
- `reports/`: consultas y evidencias de reportes.

---

## Instalación rápida

1. Crear y activar un entorno virtual.
2. Instalar dependencias desde `backend/requirements.txt`.
3. Configurar variables de entorno.
4. Ejecutar migraciones.
5. Cargar datos iniciales con `database/seed_data.py` y `database/seed_extended.py`.
6. Iniciar el servidor Django.

---

## Funcionalidades implementadas

- Autenticación de usuarios.
- Dashboard con indicadores.
- Gestión de productos.
- Registro de entradas y salidas.
- Alertas por stock bajo.
- Órdenes de compra sugeridas.
- Gestión de proveedores.
- Reportes de inventario y movimientos.

---

## Documentación clave

- [SRS IEEE 830](docs/SRS_IEEE830.md)
- [Guía UML SIGIM](docs/UML_SIGIM.md)
- [Matriz de trazabilidad](docs/matriz_trazabilidad.md)

---

## Estado actual

El repositorio quedó reorganizado para que el frontend viva dentro de `frontend/` y el backend dentro de `backend/`, alineado con la guía de entrega.
