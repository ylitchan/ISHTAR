from django.db import models


# Create your models here.

class AlphaInfo(models.Model):
    tweet_id = models.TextField(primary_key=True)
    tweet_user = models.TextField()
    tweet_alpha = models.TextField()
    tweet_text = models.TextField()
    tweet_media = models.TextField()
    tweet_gpt = models.TextField()
    alpha_time = models.TextField()
    user_thumb = models.TextField()
    tweet_time = models.TextField


class ProjectInfo(models.Model):
    username = models.TextField(primary_key=True)
    FollowedToday = models.TextField()
    Followers = models.TextField()
    Bio = models.TextField()
    Created = models.TextField()
    DiscoveryTime = models.TextField()