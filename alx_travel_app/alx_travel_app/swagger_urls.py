from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="API documentation for ALX Travel App",
        contact=openapi.Contact(email="joelkmuhoho@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
