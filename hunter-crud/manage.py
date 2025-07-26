import os
import sys


def main() -> None:
    """Run administrative tasks."""
    ALLOWED_ENVIRONMENTS = ("dev", "prod", "staging")

    environment = os.getenv("DJANGO_ENV", "dev")

    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(
            f"Invalid DJANGO_ENV: '{environment}'. Allowed values: {', '.join(ALLOWED_ENVIRONMENTS)}"  # noqa: WPS237
        )

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", f"huntercrud.settings.{environment}"
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
