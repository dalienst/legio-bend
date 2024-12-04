from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.timezone import now

from dailyverse.serializers import DailyVerseSerializer
from dailyverse.models import DailyVerse


class DailyVerseListCreateView(generics.ListCreateAPIView):
    queryset = DailyVerse.objects.all()
    serializer_class = DailyVerseSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active_date"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DailyVerseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyVerse.objects.all()
    serializer_class = DailyVerseSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"


class VerseOfTheDayView(generics.ListAPIView):
    queryset = DailyVerse.objects.filter(active_date=now().date()).first()
    serializer_class = DailyVerseSerializer
