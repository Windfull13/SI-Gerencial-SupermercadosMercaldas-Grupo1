# SIGIM — Sistema de Gestión de Inventarios Mercaldas

**Universidad de Caldas** | Sistemas de Información Gerencial  
**Integrantes:** Ángelo Franco Orozco · Shirley Ximena Ramírez López  
**Stack:** Django 4.2 · PostgreSQL · Bootstrap 5

---

## Estructura del proyecto

```
README.md
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── sigim/              # Configuración Django
│   ├── inventario/         # App principal
│   ├── proveedores/
│   ├── usuarios/
│   └── .env.example
├── frontend/
│   ├── templates/
│   └── static/
├── database/
│   ├── sigim.sql
│   ├── seed_data.py
│   └── seed_data2.py
├── docs/
├── mockups/
└── reports/
```

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
cd sigim
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
```
DB_PASSWORD=tu_contraseña_aqui
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

- ✅ Login con autenticación Django
- ✅ Dashboard con KPIs (total productos, bajo stock, sin stock, alertas)
- ✅ Lista de productos con búsqueda y filtros (nombre, categoría, estado)
- ✅ Detalle de producto con historial de movimientos
- ✅ Registro de entradas de inventario (RF-05)
- ✅ Registro de salidas con actualización automática (RF-02)
- ✅ Alertas automáticas por stock bajo (RF-04)
- ✅ Generación automática de sugerencia de orden de compra (RF-08)
- ✅ Aprobación de órdenes de compra
- ✅ Panel de administración Django en `/admin/`

---

## Módulo admin Django

Accede a `/admin/` con usuario `admin` / `admin1234` para gestión avanzada de todos los modelos.
