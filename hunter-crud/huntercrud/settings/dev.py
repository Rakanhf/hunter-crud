from huntercrud.settings.base import *  # noqa: WPS347, F403

DEBUG = True
LOGLEVEL = "DEBUG"

INSTALLED_APPS += [  # noqa: WPS407, F405
    "drf_spectacular",
]

SPECTACULAR_SETTINGS = {  # noqa: WPS407
    "TITLE": "Hunter Crud - Hunter Crud API",
    "DESCRIPTION": "A simple Hunter.io CRUD service",
    "CONTACT": {
        "name": "Rakan Farhouda",
        "email": "rakanfarhouda@icloud.com",
    },
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "REDOC_UI_SETTINGS": {"theme": "dark"},
    "COMPONENT_SPLIT_REQUEST": True,
}
