# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy_djangoitem import DjangoItem
from tools import *

class AlphaplanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TweetlItem(DjangoItem):
    # define the fields for your item here like:
    django_model = AlphaInfo

