from django.urls import path

from dailymassreading.views import (
    DailyMassReadingListCreateView,
    DailyMassReadingRetrieveUpdateDestroyView,
    DailyMassReadingListView,
    DailyMassReadingRetrieveView,
)

urlpatterns = [
    path("", DailyMassReadingListCreateView.as_view(), name="dailymassreading-list"),
    path(
        "<str:slug>/",
        DailyMassReadingRetrieveUpdateDestroyView.as_view(),
        name="dailymassreading-detail",
    ),
    path("list/", DailyMassReadingListView.as_view(), name="dailymassreading-list-view"),
    path(
        "detail/<str:reference>/",
        DailyMassReadingRetrieveView.as_view(),
        name="dailymassreading-detail-view",
    ),
]
