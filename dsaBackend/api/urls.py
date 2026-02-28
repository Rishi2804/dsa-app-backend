from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('user/register/', views.registerUser, name='user_register'),
    path('user/login/', TokenObtainPairView.as_view(), name='user_login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='user_token_refresh'),
]