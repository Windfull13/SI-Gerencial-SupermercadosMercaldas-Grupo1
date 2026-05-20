# SIGIM — Sistema de Gestión de Inventarios Mercaldas

Sistema de información gerencial para el control de inventarios del supermercado Mercaldas, desarrollado como proyecto de aula para la Universidad de Caldas.

**Integrantes:** Ángelo Franco Orozco · Shirley Ximena Ramírez López

**Stack:** Django 4.2 · PostgreSQL · Bootstrap 5

---

## Estructura del repositorio

```text
SIGIM-main/
├── README.md
├── .gitignore
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── inventario/
│   ├── proveedores/
│   ├── usuarios/
│   └── sigim/
├── database/
│   ├── sigim.sql
│   ├── seed_data.py
│   └── seed_data2.py
├── docs/
├── frontend/
│   ├── templates/
│   └── static/
├── mockups/
└── reports/
```

---

## Estructura funcional

- `backend/`: código Django, modelos, vistas, formularios y configuración.
- `database/`: dump PostgreSQL y scripts de carga de datos.
- `frontend/`: plantillas HTML y archivos estáticos del sistema.
- `docs/`: documentación del proyecto, manuales y trazabilidad.
- `mockups/`: prototipos y capturas de diseño.
- `reports/`: consultas y evidencias de reportes.

---

## Instalación rápida

1. Crear y activar un entorno virtual.
2. Instalar dependencias con `pip install -r backend/requirements.txt`.
3. Configurar variables de entorno copiando `.env.example` a `.env`.
4. Crear la base de datos `sigim_db` en PostgreSQL usando `postgres` / `1234` si no tienes un `.env` propio.
5. Ejecutar migraciones con `python backend/manage.py migrate`.
6. Cargar datos iniciales con `python backend/manage.py shell < database/seed_data.py`.
7. Iniciar el servidor con `python backend/manage.py runserver`.

---

## Instalación paso a paso

### 1. Prerrequisitos
- Python 3.10+ instalado
- PostgreSQL instalado y corriendo
- Git (opcional)

### 2. Clonar o descomprimir el proyecto
```bash
cd ~/Desktop
# Si lo descargaste como ZIP, descomprime y entra a la carpeta
cd SIGIM-main
```

### 3. Crear entorno virtual
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r backend/requirements.txt
```

### 5. Crear la base de datos en PostgreSQL
Abre pgAdmin o psql y ejecuta:
```sql
CREATE DATABASE sigim_db;
```

### 6. Configurar variables de entorno
```bash
cp .env.example .env
```
Edita el archivo `.env` con tu contraseña de PostgreSQL:
```text
DB_PASSWORD=1234
```

### 7. Ejecutar migraciones
```bash
python backend/manage.py makemigrations
python backend/manage.py migrate
```

### 8. Cargar datos iniciales
```bash
python backend/manage.py shell < database/seed_data.py
```

### 9. Iniciar el servidor
```bash
python backend/manage.py runserver
```

Abre el navegador en: **http://127.0.0.1:8000**

---

## Credenciales de acceso

| Usuario      | Contraseña | Rol                     |
|-------------|------------|-------------------------|
| `admin`     | `admin1234`| Superusuario (admin)    |
| `encargado` | `1234`     | Encargado de inventario |
| `cajero1`   | `1234`     | Cajero                  |

---

## Funcionalidades implementadas

- Login con autenticación Django.
- Dashboard con KPIs de inventario.
- Lista de productos con búsqueda y filtros.
- Detalle de producto con historial de movimientos.
- Registro de entradas y salidas de inventario.
- Alertas automáticas por stock bajo.
- Generación de sugerencias de orden de compra.
- Aprobación de órdenes de compra.
- Panel de administración Django en `/admin/`.

---

## Documentación clave

- [SRS IEEE 830](docs/SRS_IEEE830.md)
- [Guía UML SIGIM](docs/UML_SIGIM.md)
- [Matriz de trazabilidad](docs/matriz_trazabilidad.md)

---

## Estado actual

El repositorio ya quedó reorganizado para que el backend viva en `backend/`, el frontend en `frontend/`, y los datos y scripts en `database/`, dejando `docs/`, `mockups/` y `reports/` como carpetas independientes.
