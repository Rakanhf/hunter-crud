# Base stage
FROM python:3.10.12-slim AS base

ARG DJANGO_ENV

# Environment variables
ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.8.3 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'


# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION" && poetry --version

# Set the working directory to the project
WORKDIR /app

COPY hunter-crud/pyproject.toml hunter-crud/poetry.lock /app/

# Install dependencies:
RUN poetry install

# Copy the project
COPY hunter-crud/ /app

# Copy Scripts
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Command to start the application
ENTRYPOINT ["entrypoint.sh"]
