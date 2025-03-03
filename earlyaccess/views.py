from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import generics

from earlyaccess.models import EarlyAccess
from earlyaccess.serializers import EarlyAccessSerializer


class EarlyAccessCreateView(generics.CreateAPIView):
    queryset = EarlyAccess.objects.all()
    serializer_class = EarlyAccessSerializer
    permission_classes = (AllowAny,)


class EarlyAccessListView(generics.ListAPIView):
    queryset = EarlyAccess.objects.all()
    serializer_class = EarlyAccessSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]


class EarlyAccessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EarlyAccess.objects.all()
    serializer_class = EarlyAccessSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs.get("slug"))
