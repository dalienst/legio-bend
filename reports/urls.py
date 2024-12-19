from django.urls import path

from reports.views import (
    ReportCreateView,
    ReportListView,
    ReportRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("create/", ReportCreateView.as_view(), name="create"),
    path("", ReportListView.as_view(), name="list"),
    path("<str:slug>/", ReportRetrieveUpdateDestroyView.as_view(), name="detail"),
]
