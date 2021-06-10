FROM python:3.8

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/
COPY ./scripts/start_worker.sh /app/scripts/start_worker.sh

RUN bash -c "poetry install --no-root --no-dev"

RUN chmod +x /app/scripts/start_worker.sh

CMD ["bash", "/app/scripts/start_worker.sh"]