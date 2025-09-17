from django.urls import path

from teachings.views import TeachingListCreateView, TeachingDetailView

urlpatterns = [
    path("", TeachingListCreateView.as_view(), name="teaching-list"),
    path(
        "<str:identity>/",
        TeachingDetailView.as_view(),
        name="teaching-detail",
    ),
]
