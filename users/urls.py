from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("profile/", views.profile, name="profile"),
    path("setting/", views.setting, name="setting"),
    path("feedback/", views.feedback, name="feedback"),
    path("coupon/", views.coupon, name = "coupon"),
    path("register/", views.register, name="register"),
    path("login/", views.my_login, name="login"),
    path("logout/", views.my_logout, name="logout"),
]
