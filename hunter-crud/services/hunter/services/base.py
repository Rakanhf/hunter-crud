import requests
from typing import TYPE_CHECKING, Any
from services.hunter.config import BASE_URL

if TYPE_CHECKING:
    from services.hunter.client import HunterClient


class BaseService:
    def __init__(self, client: "HunterClient"):
        self._client = client

    def _url(self, path: str) -> str:
        return f"{BASE_URL}/{path}"

    def _get(self, path: str, **kwargs: Any) -> requests.Response:
        if "params" not in kwargs:
            kwargs["params"] = {}
        kwargs["params"]["api_key"] = self._client.api_key
        return self._client.session.get(self._url(path), **kwargs)
