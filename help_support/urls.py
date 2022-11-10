from django.urls import path
from .views import create_issue, home


urlpatterns = [
    path("", home, name="home"),
    path("issues/create/", create_issue, name="issue-create"),
]