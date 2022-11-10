from django.db import models
from django.contrib.auth.models import AbstractUser
from help_support.models import Department, Issue


class User(AbstractUser):
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL)
