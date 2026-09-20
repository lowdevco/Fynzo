from django.urls import path
from .views import CookieTokenObtainPairView, CookieTokenRefreshView

urlpatterns = [
    path('api/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]
