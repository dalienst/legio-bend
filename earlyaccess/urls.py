from django.urls import path

from earlyaccess.views import (
    EarlyAccessCreateView,
    EarlyAccessDetailView,
    EarlyAccessListView,
)

urlpatterns = [
    path("create/", EarlyAccessCreateView.as_view(), name="create"),
    path("", EarlyAccessListView.as_view(), name="list"),
    path("<str:slug>/", EarlyAccessDetailView.as_view(), name="detail"),
]
