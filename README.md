
-----------------------
# Run test server
python3 manage.py

-----------------------
# Cambios en estructuras de base de datos

## Para levantar de cero el proyecto
CREATE DATABASE fabricaserra;
CREATE USER serra WITH PASSWORD 'serra123';
GRANT ALL PRIVILEGES ON DATABASE fabricaSerra TO serra;
ALTER DATABASE fabricaserra OWNER TO serra;
