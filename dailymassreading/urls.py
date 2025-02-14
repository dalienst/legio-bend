from django.urls import path

from dailymassreading.views import (
    DailyMassReadingListCreateView,
    DailyMassReadingRetrieveUpdateDestroyView,
    DailyMassReadingListView,
    DailyMassReadingRetrieveView,
    MassOfTheDayView,
)

urlpatterns = [
    path("", DailyMassReadingListCreateView.as_view(), name="dailymassreading-list"),
    path(
        "<str:slug>/",
        DailyMassReadingRetrieveUpdateDestroyView.as_view(),
        name="dailymassreading-detail",
    ),
    path(
        "list/", DailyMassReadingListView.as_view(), name="dailymassreading-list-view"
    ),
    path("mass/list/", MassOfTheDayView.as_view(), name="mass-of-the-day"),
    path(
        "detail/<str:reference>/",
        DailyMassReadingRetrieveView.as_view(),
        name="dailymassreading-detail-view",
    ),
]
