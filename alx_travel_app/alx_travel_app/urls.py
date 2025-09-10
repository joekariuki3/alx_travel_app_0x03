from django.contrib import admin
from django.urls import path, include
from . import swagger_urls
from listings import urls as listings_urls
from listings.views import LogoutView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(swagger_urls.urlpatterns)),
    path('api/', include(listings_urls.urlpatterns)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
]
