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


class VerseOfTheDayView(APIView):
    def get(self, request, *args, **kwargs):
        today = now().date()
        verse = DailyVerse.objects.filter(active_date=today).first()
        if verse:
            return Response(DailyVerseSerializer(verse).data, status=200)
        return Response({"message": "No verse of the day available."}, status=404)
