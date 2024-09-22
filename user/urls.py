from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.apps import UserConfig
from user.views import UserViewSet

app_name = UserConfig.name

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(permission_classes=[AllowAny]), name="token_obtain_pair",),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh",),
] + router.urls
