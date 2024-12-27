from django.urls import path

from accounts.views import (
    LogoutView,
    SignInView,
    UserDetailView,
    UserCreateView,
    StaffUserCreateView,
    VerifyEmailView,
    RequestPasswordResetView,
    PasswordResetView,
    UserListView,
    UserRetrieveView,
)

urlpatterns = (
    path("token/", SignInView.as_view(), name="login"),
    path("signup/", UserCreateView.as_view(), name="register"),
    path("signup/staff/", StaffUserCreateView.as_view(), name="staff_register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("verify-account/", VerifyEmailView.as_view(), name="verify-email"),
    path("<str:id>/", UserDetailView.as_view(), name="user_detail"),
    path("password/reset/", RequestPasswordResetView.as_view(), name="password-reset"),
    path("password/new/", PasswordResetView.as_view(), name="password-reset"),
    path("", UserListView.as_view(), name="user-list"),
    path("users/<str:slug>/", UserRetrieveView.as_view(), name="user-detail"),
)
