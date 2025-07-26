from django.db import models


class EmailVerificationStatus(models.TextChoices):
    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"
    ACCEPT_ALL = "accept_all"
    WEBMAIL = "webmail"
    DISPOSABLE = "disposable"


class EmailVerification(models.Model):
    email = models.EmailField(unique=True, help_text="The email address to verify")
    status = models.CharField(
        max_length=255,  # noqa: WPS432
        choices=EmailVerificationStatus.choices,
        help_text="The status of the email verification",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the email verification was created",
    )

    class Meta:
        verbose_name = "Email Verification"
        verbose_name_plural = "Email Verifications"

    def __str__(self) -> str:
        return self.email
