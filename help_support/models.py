from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Issue(models.Model):
    # status constants
    NEW = "new"
    PROGRESS = "in progress"
    RESOLVED = "resolved"

    # source constants
    WEB = "web"
    LINE = "line"
    MOBILE = "mobile"

    STATUS_CHOICES = [
        (NEW, "new"),
        (PROGRESS, "in progress"),
        (RESOLVED, "resolved"),
    ]
    SOURCE_CHOICES = [
        (WEB, "website platform"),
        (LINE, "LINE platform"),
        (MOBILE, "mobile app platform"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=NEW,
    )
    source = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES,
    )
    file = models.FileField(
        upload_to='customer_uploads/',
        validators=[FileExtensionValidator([
            'png', 'jpg', # images
            'mp4', # videos
        ])]
    )
    department = models.ManyToManyField(Department)
    software_version = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title
