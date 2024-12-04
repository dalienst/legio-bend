from django.urls import path

from dailyverse.views import (
    DailyVerseListCreateView,
    DailyVerseRetrieveUpdateDestroyView,
    VerseOfTheDayView,
)

app_name = "dailyverse"

urlpatterns = [
    path("", DailyVerseListCreateView.as_view(), name="dailyverse-list"),
    path(
        "list/",
        VerseOfTheDayView.as_view(),
        name="verse-of-the-day",
    ),
    path(
        "<str:slug>/",
        DailyVerseRetrieveUpdateDestroyView.as_view(),
        name="dailyverse-detail",
    ),
]
