from django.db import models
from django.conf import settings
from user_profiles.models import UserProfile


# Create your models here.
class ProgressPost(models.Model):

    post_title = models.CharField(max_length=60, null=False, blank=False)
    post_content = models.CharField(max_length=2000, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                               null=True, related_name='posts', editable=False)

    def __str__(self):
        return self.post_title


class Comment(models.Model):

    post = models.ForeignKey(ProgressPost, null=False, blank=False, on_delete=models.CASCADE, related_name='comments', editable=False)
    comment_content = models.CharField(max_length=400, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                               null=True, related_name='comments', editable=False)

    def __str__(self):
        return self.comment_content
