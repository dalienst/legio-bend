from django.urls import path

from highlights.views import HighlightListCreateView, HighlightRetrieveUpdateDestroyView

app_name = "highlights"

urlpatterns = [
    path("", HighlightListCreateView.as_view(), name="highlight-list"),
    path(
        "<str:slug>/",
        HighlightRetrieveUpdateDestroyView.as_view(),
        name="highlight-detail",
    ),
]
