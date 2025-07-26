from rest_framework import serializers
from api.models import EmailVerification


class EmailverificationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(help_text="The email address to verify")


class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerification
        fields = "__all__"
        read_only_fields = ["created_at"]
