from django.urls import path

from accounts.views import (
    LogoutView,
    TokenView,
    UserDetailView,
    UserCreateView,
)

urlpatterns = (
    path("token/", TokenView.as_view(), name="token_obtain_pair"),
    path("signup/", UserCreateView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:id>/", UserDetailView.as_view(), name="user_detail"),
)
