from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from .views import TemperatureAPIView
schema_view = get_schema_view(
    openapi.Info(
        title="Weahter API",
        default_version='v1',
        description="The official Weather Test API documentation",
        contact=openapi.Contact(email="kevin.nzioka.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('locations/<str:city>/', TemperatureAPIView.as_view(),
         name='temparature-stats'),
]
