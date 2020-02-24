from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('auth.urls')),
    url('', include('boats.urls')),
    url('', include('cars.urls')),
    url('', include('trucks.urls')),
]