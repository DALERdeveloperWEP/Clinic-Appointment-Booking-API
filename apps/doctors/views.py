from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import TimeSlot
from .serializers import TimeSlotSerializer
from ..users.permissions import IsDoctor, IsOwnerByDoctor


class TimeSlotViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsDoctor, IsOwnerByDoctor]

    serializer_class = TimeSlotSerializer    
    
    def get_queryset(self):
        queryset = TimeSlot.objects.all()
        return queryset.filter(doctor=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)
        return super().perform_create(serializer)