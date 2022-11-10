from django.urls import path
from .views import register, signin, signout, admin_signin

urlpatterns = [
    path("signup/", register, name="signup"),
    path("signin/", signin, name="signin"),
    path("signout", signout, name="signout"),
    path("admin/signin/", admin_signin, name="admin_signin")
]