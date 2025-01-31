from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from dailymassreading.models import DailyMassReading
from dailymassreading.serializers import DailyMassReadingSerializer


# Authenticated views
class DailyMassReadingListCreateView(generics.ListCreateAPIView):
    queryset = DailyMassReading.objects.all()
    serializer_class = DailyMassReadingSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]


class DailyMassReadingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyMassReading.objects.all()
    serializer_class = DailyMassReadingSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"


# Public views
class DailyMassReadingListView(generics.ListAPIView):
    queryset = DailyMassReading.objects.all()
    serializer_class = DailyMassReadingSerializer
    permission_classes = [
        AllowAny,
    ]


class DailyMassReadingRetrieveView(generics.RetrieveAPIView):
    queryset = DailyMassReading.objects.all()
    serializer_class = DailyMassReadingSerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "reference"
