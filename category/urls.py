from django.urls import path

from category.views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    CategoryListView,
    CategoryRetrieveView,
)

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="category-list"),
    path(
        "<str:slug>/",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-detail",
    ),
    path("categories/list/", CategoryListView.as_view(), name="category-list-view"),
    path(
        "detail/<str:reference>/",
        CategoryRetrieveView.as_view(),
        name="category-detail-view",
    ),
]
