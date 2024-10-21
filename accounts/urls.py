from django.urls import path

from accounts.views import (
    LogoutView,
    SignInView,
    UserDetailView,
    UserCreateView,
)

urlpatterns = (
    path("token/", SignInView.as_view(), name="login"),
    path("signup/", UserCreateView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:id>/", UserDetailView.as_view(), name="user_detail"),
)
