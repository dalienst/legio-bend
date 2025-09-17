from rest_framework import generics

from teachings.models import Teaching
from teachings.serializers import TeachingSerializer
from accounts.permissions import IsAdminOrReadOnly


class TeachingListCreateView(generics.ListCreateAPIView):
    queryset = Teaching.objects.all()
    serializer_class = TeachingSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TeachingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teaching.objects.all()
    serializer_class = TeachingSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = "identity"
