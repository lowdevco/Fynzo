from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from rest_framework.response import Response

class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            
            response.set_cookie(
                'access_token',
                access_token,
                httponly=True,
                samesite='Lax'
            )
            response.set_cookie(
                'refresh_token',
                refresh_token,
                httponly=True,
                samesite='Lax'
            )
        return response

class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Extract refresh token from cookie if not in body
        if 'refresh' not in request.data and 'refresh_token' in request.COOKIES:
            request.data['refresh'] = request.COOKIES['refresh_token']
            
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data.get('access')
            response.set_cookie(
                'access_token',
                access_token,
                httponly=True,
                samesite='Lax'
            )
        return response
