# FabricaSerra Admin

## Descripción
Extensión de Invoice Ninja para digitalización integral de empresa, enfocada en:
- Control de producción de productos
- Punto de venta 
- Generación de reportes avanzados

Proyecto construido con Django y postgresql.

## Arquitectura del Proyecto
- Backend: Django
- Base de Datos: PostgreSQL
- Contenedorización: Docker
- Gestión de Dependencias: Poetry
- Lenguaje: Python 3.8+

## Requisitos Previos
- Docker (19.03.0+)
- Docker Compose (1.27.0+)
- Poetry (1.2.0+)
- Python 3.8-3.11
- Git

## Configuración Inicial

### Clonar Repositorio
```bash
git clone https://github.com/agusserraalh/fabricaAdmin.git
cd fabricaAdmin
```

### Variables de Entorno
```bash
# Copiar template de configuración
cp .env.example .env

# Editar configuraciones sensibles
nano .env
```

### Docker-compose

#### Construir Servicios
```bash
# Construir y levantar contenedores
docker-compose up --build -d

# Ver estado de contenedores
docker-compose ps
```

#### Configuración Inicial de Base de Datos
```bash
# Crear base de datos y usuario - Revisar que no anda desde afuera
docker-compose exec postgres psql -U postgres -c """
CREATE DATABASE fabricaserra;
CREATE USER serra WITH PASSWORD 'serra123';
GRANT ALL PRIVILEGES ON DATABASE fabricaSerra TO serra;
ALTER DATABASE fabricaserra OWNER TO serra;
"""

# Aplicar migraciones
docker-compose exec web python manage.py migrate

# Crear superusuario
docker-compose exec web python manage.py createsuperuser
```

#### Iniciar Servidor
```bash
# Modo desarrollo
docker compose exec web python manage.py runserver 0.0.0.0:8000

# Modo background
docker-compose exec web python manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &
```

### Instalación Local 

#### Configurar Poetry
```bash
# Instalar Poetry
pip install poetry

# Instalar dependencias
poetry install

# Activar entorno virtual
poetry shell
```

#### Configuración Inicial de Base de Datos

Mismos pasos que en docker-compose solo que sin los comandos de docker compose.

#### Iniciar Servidor
```bash
# Modo desarrollo
python manage.py runserver 0.0.0.0:8000

# Modo background
python manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &
```

## Desarrollo y Calidad de Código



## Estructura de Directorios

## Seguridad

### Consideraciones
- Usar variables de entorno para credenciales
- Deshabilitar DEBUG en producción
- Configurar CORS y CSRF
- Implementar autenticación robusta

### Actualización de Dependencias
```bash
# Verificar actualizaciones
poetry show --latest

# Actualizar dependencias
poetry update
```

## Despliegue


### Comandos Útiles
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Crear respaldos de base de datos
pg_dump -U serra fabricaserra > backup.sql

# Verificar proceso
jobs -l
ps aux | grep manage.py
```


## Contacto
- Autor: Agustín Serra
- Email: agustin.sebastian.serra@gmail.com
- GitHub: @agusserraalh
```

