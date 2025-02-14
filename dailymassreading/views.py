from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView

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


class MassOfTheDayView(APIView):
    def get(self, request, *args, **kwargs):
        today = now().date()
        mass = DailyMassReading.objects.filter(mass_date=today).first()
        if mass:
            return Response(DailyMassReadingSerializer(mass).data, status=200)
        return Response({"message": "No mass of the day available."}, status=404)


class DailyMassReadingRetrieveView(generics.RetrieveAPIView):
    queryset = DailyMassReading.objects.all()
    serializer_class = DailyMassReadingSerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "reference"
