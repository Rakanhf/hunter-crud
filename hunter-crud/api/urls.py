from api.views import EmailVerificationViewSet
from rest_framework.routers import DefaultRouter

app_name = "api"
router = DefaultRouter()

router.register(
    r"email-verifications", EmailVerificationViewSet, basename="email-verifications"
)

urlpatterns = router.urls
