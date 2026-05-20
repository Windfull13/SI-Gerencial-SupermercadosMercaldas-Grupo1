# Database

Archivos de base de datos del proyecto SIGIM.

## Contenido
- `sigim.sql`: dump PostgreSQL completo con esquema y datos.
- `seed_data.py`: carga inicial con Django ORM.
- `seed_data2.py`: carga alternativa o complementaria con Django ORM.
- `seed_extended.py`: poblado adicional para alcanzar volumen de prueba.

## Restaurar PostgreSQL
1. Crear la base `sigim_db` en PostgreSQL.
2. Restaurar `sigim.sql` con pgAdmin o `psql`.
3. Ajustar `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` y `DB_PORT` en `backend/.env`.

## Carga por ORM
Desde `backend/`:

```bash
python manage.py migrate
python ..\database\seed_data.py
python ..\database\seed_extended.py
```
