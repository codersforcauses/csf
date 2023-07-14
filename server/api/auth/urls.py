from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views


app_name = 'auth'

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="jwt_token"),
    path("refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path("register/", views.register, name="register"),
]
