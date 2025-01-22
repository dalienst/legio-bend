from django.urls import path

from subcategory.views import (
    SubcategoryListCreateAPIView,
    SubcategoryRetrieveUpdateDestroyAPIView,
    SubcategoryListAPIView,
    SubcategoryRetrieveAPIView,
)

urlpatterns = [
    # Authenticated endpoints
    path("", SubcategoryListCreateAPIView.as_view(), name="subcategory-list-create"),
    path(
        "<str:slug>/",
        SubcategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="subcategory-retrieve-update-destroy",
    ),
    # Public endpoints
    path(
        "subcategories/list/", SubcategoryListAPIView.as_view(), name="subcategory-list"
    ),
    path(
        "detail/<str:reference>/",
        SubcategoryRetrieveAPIView.as_view(),
        name="subcategory-retrieve",
    ),
]
