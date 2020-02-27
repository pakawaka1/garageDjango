from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('auth.urls')),
    url('', include('boats.urls')),
    url('', include('cars.urls')),
    url('', include('trucks.urls')),
    url('api/token/', jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    url('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'),
    url('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),

]
