from django.db import models
from django.utils import timezone
from account.models import CustomUser

# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(CustomUser, related_name="tweet_likes", blank=True)

    def __str__(self):
        return self.content[:5]


class Comment(models.Model):
    post_connected = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(CustomUser, related_name="comment_likes", blank=True)

    def __str__(self):
        return self.content[:5]

