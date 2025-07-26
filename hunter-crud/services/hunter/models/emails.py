from enum import Enum
from pydantic import BaseModel


class EmailVerificationStatus(str, Enum):
    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"
    ACCEPT_ALL = "accept_all"
    WEBMAIL = "webmail"
    DISPOSABLE = "disposable"


class EmailVerification(BaseModel):
    email: str
    status: EmailVerificationStatus
