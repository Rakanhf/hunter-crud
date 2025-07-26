import logging

import coloredlogs
import verboselogs

from django.conf import settings

# Set up logger
logging.basicConfig(level=settings.LOGLEVEL)  # pragma: no cover
logger = verboselogs.VerboseLogger(__name__)  # pragma: no cover
coloredlogs.install()  # pragma: no cover
