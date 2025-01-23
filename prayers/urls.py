from django.urls import path

from prayers.views import (
    PrayerListCreateView,
    PrayerRetrieveUpdateDestroyView,
    PrayerListView,
    PrayerRetrieveView,
)

urlpatterns = [
    path("", PrayerListCreateView.as_view(), name="prayer-list-create"),
    path(
        "<str:slug>/",
        PrayerRetrieveUpdateDestroyView.as_view(),
        name="prayer-retrieve-update-destroy",
    ),
    path("prayer/list/", PrayerListView.as_view(), name="prayer-list"),
    path(
        "detail/<str:reference>/", PrayerRetrieveView.as_view(), name="prayer-retrieve"
    ),
]
