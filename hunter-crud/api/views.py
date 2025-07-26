from django.conf import settings
from typing import Any
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from api.models import EmailVerification
from api.serializers import (
    EmailVerificationSerializer,
    EmailverificationRequestSerializer,
)
from huntercrud.logging import logger
from services.hunter.client import HunterClient


class EmailVerificationViewSet(ModelViewSet):
    serializer_class = EmailVerificationSerializer
    queryset = EmailVerification.objects.all()

    http_method_names = ["get", "post", "delete"]

    @extend_schema(
        summary="Verify an email address",
        description="Verify an email address using the Hunter.io API",
        responses={200: EmailVerificationSerializer},
        request=EmailverificationRequestSerializer,
    )
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = EmailverificationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_instance = EmailVerification.objects.filter(
            email=serializer.validated_data["email"]
        ).first()
        if email_instance:
            return Response(
                self.get_serializer(email_instance).data, status=status.HTTP_200_OK
            )
        client = HunterClient(api_key=settings.HUNTER_API_KEY)
        try:
            response = client.emails.verify(serializer.validated_data["email"])
        except Exception as exception:
            logger.error(f"Error verifying email: {exception}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response:
            serializer = self.get_serializer(data=response.model_dump())
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
