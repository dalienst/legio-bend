from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (AllowAny,)


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "report_type",
    ]


class ReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs.get("slug"))
