#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

if [ "$RUN_MIGRATIONS" = "True" ]; then
    # Make migrations and migrate
    echo "Making migrations..."
    python manage.py check --deploy
    python manage.py makemigrations --no-input
    python manage.py showmigrations
    python manage.py migrate --no-input
fi

# If we reached here without starting Gunicorn, run whatever command was passed in
echo "⚙️  Entrypoint handing off to: $@"
exec "$@"