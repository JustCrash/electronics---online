from rest_framework import routers

from company.apps import CompanyConfig
from company.views import CompanyViewSet

app_name = CompanyConfig.name

router = routers.DefaultRouter()
router.register(r"company", CompanyViewSet, basename="company")

urlpatterns = [] + router.urls
