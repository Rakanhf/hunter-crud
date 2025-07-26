import os
from django.core.asgi import get_asgi_application

ALLOWED_ENVIRONMENTS = ("dev", "prod", "staging")
environment = os.getenv("DJANGO_ENV", "dev")

if environment not in ALLOWED_ENVIRONMENTS:
    raise ValueError(
        f"Invalid DJANGO_ENV: '{environment}'. Allowed values: {', '.join(ALLOWED_ENVIRONMENTS)}"  # noqa: WPS237
    )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"huntercrud.settings.{environment}")

application = get_asgi_application()
