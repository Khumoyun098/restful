from django.urls import include, path
from rest_framework import routers
from api import views
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
    openapi.Info(
        title="Restful API",
        default_version='v1',
    ),
    public=False
)


router = routers.DefaultRouter()
router.register(prefix='cars', viewset=views.CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]