from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    text_type = models.CharField(max_length=20, blank=True, null=True)
    tags = TaggableManager()    # タグ用フィールド

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
