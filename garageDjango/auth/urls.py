from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^auth/login', views.login_user, name="login"),
    url(r'^auth/user', views.user, name="user")

]
