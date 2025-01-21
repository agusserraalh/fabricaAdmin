FROM python:3

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    mv /root/.local/bin/poetry /usr/local/bin/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false

RUN poetry install --no-root 

COPY . /code/

RUN poetry 

CMD ["tail", "-f", "/dev/null"]
