from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('auth', views.AuthView)

urlpatterns = [
    url('/', includes(router.urls)),
    url('/login', includes(login.urls)),
    url('/user', includes(user.urls),
    url('/logout', includes(logout.urls),

]