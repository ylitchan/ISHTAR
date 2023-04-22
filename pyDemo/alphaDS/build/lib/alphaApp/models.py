from django.db import models

# Create your models here.

class AlphaInfo(models.Model):
    """
    股票信息
    """

    tweet_id = models.TextField()
    tweet_user = models.TextField()
    tweet_text = models.TextField()
    tweet_media = models.TextField()
    tweet_gpt = models.TextField()
    alpha_time = models.TextField()

