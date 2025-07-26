from services.hunter.services.base import BaseService
from services.hunter.models.emails import EmailVerification


class EmailsService(BaseService):
    """
    Service for interacting with the Hunter.io email APIs.
    """

    def verify(self, email: str) -> EmailVerification | None:
        """
        Allows you to verify the deliverability of an email address.
        """
        verification_params = {"email": email}
        response = self._get("email-verifier", params=verification_params)
        response_data = response.json()
        if response_data["data"]:
            return EmailVerification.model_validate(response_data["data"])
        return None
