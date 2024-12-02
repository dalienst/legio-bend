from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from highlights.serializers import HighlightSerializer
from highlights.models import Highlight


class HighlightListCreateView(generics.ListCreateAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class HighlightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "slug"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
