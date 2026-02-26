from rest_framework.routers import DefaultRouter
from .views import TimeSlotViewSet

router = DefaultRouter()
router.register("doctors", TimeSlotViewSet, basename="timeslot")

urlpatterns = router.urls