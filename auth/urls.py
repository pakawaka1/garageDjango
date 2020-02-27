from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url('auth/login', views.LoginUser.as_view()),
    # url('auth/logout/', views.LogoutUser,
    # url('auth/register', views.RegisterUser.as_view()),
    url('hello/', views.HelloView.as_view(), name='hello'),

]
