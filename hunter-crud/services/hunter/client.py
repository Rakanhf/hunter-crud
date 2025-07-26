import requests
from services.hunter.services.emails import EmailsService


class HunterClient:
    """
    Client for interacting with the Hunter.io API.

    This client handles authentication and exposes methods to interact with the Hunter.io API.

    ---
    Example:
        ```python
        client = HunterClient(api_key='your_api_key')
        ```
    """

    def __init__(
        self,
        api_key: str,
    ):
        self.api_key = api_key
        self.session = requests.Session()
        self.emails = EmailsService(self)
