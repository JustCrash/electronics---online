from rest_framework import routers

from product.apps import ProductConfig
from product.views import ProductViewSet

app_name = ProductConfig.name

router = routers.DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [] + router.urls
