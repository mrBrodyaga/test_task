from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MaterialViewSet, СategoryViewSet


router = DefaultRouter()

router.register(r"material", MaterialViewSet, basename="material")
router.register(r"category", СategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]
