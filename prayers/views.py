from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from prayers.models import Prayer
from prayers.serializers import PrayerSerializer

"""
Authenticated views
"""


class PrayerListCreateView(generics.ListCreateAPIView):
    queryset = Prayer.objects.all()
    serializer_class = PrayerSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]


class PrayerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prayer.objects.all()
    serializer_class = PrayerSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"


"""
Public Views
"""


class PrayerListView(generics.ListAPIView):
    queryset = Prayer.objects.filter(is_public=True)
    serializer_class = PrayerSerializer
    permission_classes = [
        AllowAny,
    ]

    def get_queryset(self):
        return Prayer.objects.filter(is_public=True)


class PrayerRetrieveView(generics.RetrieveAPIView):
    queryset = Prayer.objects.filter(is_public=True)
    serializer_class = PrayerSerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "reference"
