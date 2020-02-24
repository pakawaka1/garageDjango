from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('auth', views.AuthView)

urlpatterns = [
    url('', include(router.urls)),
    url('login/', include(router.urls)),
    url('user/', include(router.urls)),
    url('logout/', include(router.urls))
]
