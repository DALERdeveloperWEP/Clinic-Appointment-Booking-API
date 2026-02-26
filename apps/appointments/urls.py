from rest_framework.routers import DefaultRouter
from .views import AppointmentsViewSet

router = DefaultRouter()

router.register('', AppointmentsViewSet, basename='appointment')

urlpatterns = router.urls
