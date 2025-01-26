FROM python:3

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    mv /root/.local/bin/poetry /usr/local/bin/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./ /code/

RUN ls /code

RUN poetry config virtualenvs.create false

RUN poetry install --no-root 

RUN poetry 

CMD ["tail", "-f", "/dev/null"]
