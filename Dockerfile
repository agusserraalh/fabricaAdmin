# syntax=docker/dockerfile:1
FROM python:3

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    mv /root/.local/bin/poetry /usr/local/bin/

# Configuración de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /code

# Copiar archivos de configuración de Poetry
COPY pyproject.toml poetry.lock /code/

# Instalar dependencias
RUN poetry config virtualenvs.create false

RUN poetry install --no-root 

# Copiar el resto del código fuente
COPY . /code/

RUN poetry 
# Comando por defecto

#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

CMD ["tail", "-f", "/dev/null"]
