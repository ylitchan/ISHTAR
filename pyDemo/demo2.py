import datetime
import json
import re
import time
import jsonpath_ng
import requests
import telebot
import tweepy

# 填写您的OAuth凭据
# consumer_key = "EmKz4uoHX8hlIql2GuuUMWHt4"
# consumer_secret = "hx40VlEMGTiubguZytjPyvamIu0xlhLp2CJqikRIN0hptuYAO5"
# access_token = "1568898000654680064-nLFjD70osgo5KCl2NjE9VznjoNtehm"
# access_token_secret = "mBOOwr2lUbDVkq0ERUnagq89mBOKkRWMu5jiDv9IT8Ed8"
#
# # 创建API对象并进行身份验证
# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# api = tweepy.API(auth)
#
# # 添加单个成员
# list_id = 1613599219830657025  # 要添加成员的列表ID
# user_id = 1482569282777190403  # 要添加的用户ID
# a=api.remove_list_member(list_id=list_id, user_id=user_id)
# print(a)
from dateutil import parser
# only = {
#     "entryId": "tweet-1647010884370198528",
#     "sortIndex": "1647052074975756285",
#     "content": {
#         "entryType": "TimelineTimelineItem",
#         "__typename": "TimelineTimelineItem",
#         "itemContent": {
#             "itemType": "TimelineTweet",
#             "__typename": "TimelineTweet",
#             "tweet_results": {
#                 "result": {
#                     "__typename": "Tweet",
#                     "rest_id": "1647010884370198528",
#                     "core": {
#                         "user_results": {
#                             "result": {
#                                 "__typename": "User",
#                                 "id": "VXNlcjoxNjM5NjY1MTU0OTkxMzA4ODAw",
#                                 "rest_id": "1639665154991308800",
#                                 "affiliates_highlighted_label": {},
#                                 "has_graduated_access": 'False',
#                                 "is_blue_verified": 'False',
#                                 "profile_image_shape": "Circle",
#                                 "legacy": {
#                                     "following": 'true',
#                                     "can_dm": 'False',
#                                     "can_media_tag": 'true',
#                                     "created_at": "Sat Mar 25 16:26:58 +0000 2023",
#                                     "default_profile": 'true',
#                                     "default_profile_image": 'False',
#                                     "description": "The magic starts here",
#                                     "entities": {
#                                         "description": {
#                                             "urls": []
#                                         },
#                                         "url": {
#                                             "urls": [
#                                                 {
#                                                     "display_url": "app.mute.io/swap",
#                                                     "expanded_url": "https://app.mute.io/swap",
#                                                     "url": "https://t.co/fJK9vPLl6w",
#                                                     "indices": [
#                                                         0,
#                                                         23
#                                                     ]
#                                                 }
#                                             ]
#                                         }
#                                     },
#                                     "fast_followers_count": 0,
#                                     "favourites_count": 31,
#                                     "followers_count": 8492,
#                                     "friends_count": 21,
#                                     "has_custom_timelines": 'False',
#                                     "is_translator": 'False',
#                                     "listed_count": 24,
#                                     "location": "",
#                                     "media_count": 0,
#                                     "name": "POupi",
#                                     "normal_followers_count": 8492,
#                                     "pinned_tweet_ids_str": [],
#                                     "possibly_sensitive": 'False',
#                                     "profile_banner_url": "https://pbs.twimg.com/profile_banners/1639665154991308800/1680630241",
#                                     "profile_image_url_https": "https://pbs.twimg.com/profile_images/1643308449206247438/V5uxhyLr_normal.jpg",
#                                     "profile_interstitial_type": "",
#                                     "screen_name": "p_oupi",
#                                     "statuses_count": 33,
#                                     "translator_type": "none",
#                                     "url": "https://t.co/fJK9vPLl6w",
#                                     "verified": 'False',
#                                     "want_retweets": 'true',
#                                     "withheld_in_countries": []
#                                 }
#                             }
#                         }
#                     },
#                     "unmention_data": {},
#                     "edit_control": {
#                         "edit_tweet_ids": [
#                             "1647010884370198528"
#                         ],
#                         "editable_until_msecs": "1681514769473",
#                         "is_edit_eligible": 'False',
#                         "edits_remaining": "5"
#                     },
#                     "edit_perspective": {
#                         "favorited": 'False',
#                         "retweeted": 'False'
#                     },
#                     "is_translatable": 'true',
#                     "views": {
#                         "state": "Enabled"
#                     },
#                     "source": "<a href=\"https://twitter.com/\" rel=\"nofollow\">Beeessss11644388432360230912a</a>",
#                     "legacy": {
#                         "bookmark_count": 0,
#                         "bookmarked": 'False',
#                         "created_at": "Fri Apr 14 22:56:09 +0000 2023",
#                         "conversation_id_str": "1647010884370198528",
#                         "display_text_range": [
#                             0,
#                             92
#                         ],
#                         "entities": {
#                             "media": [
#                                 {
#                                     "display_url": "pic.twitter.com/JBE6ekCYuK",
#                                     "expanded_url": "https://twitter.com/PaddasFinance/status/1647010774638907392/photo/1",
#                                     "id_str": "1647010609387454464",
#                                     "indices": [
#                                         69,
#                                         92
#                                     ],  # https://pbs.twimg.com/tweet_video_thumb/FtrE2OsXsAMPGMl.jpg
#                                     "media_url_https": "https://pbs.twimg.com/media/FttbbEnWwAAxAIi.jpg",
#                                     "source_status_id_str": "1647010774638907392",
#                                     "source_user_id_str": "1630090542758477824",
#                                     "type": "photo",
#                                     "url": "https://t.co/JBE6ekCYuK",
#                                     "sizes": {
#                                         "large": {
#                                             "h": 924,
#                                             "w": 1640,
#                                             "resize": "fit"
#                                         },
#                                         "medium": {
#                                             "h": 676,
#                                             "w": 1200,
#                                             "resize": "fit"
#                                         },
#                                         "small": {
#                                             "h": 383,
#                                             "w": 680,
#                                             "resize": "fit"
#                                         },
#                                         "thumb": {
#                                             "h": 150,
#                                             "w": 150,
#                                             "resize": "crop"
#                                         }
#                                     },
#                                     "original_info": {
#                                         "height": 924,
#                                         "width": 1640,
#                                         "focus_rects": [
#                                             {
#                                                 "x": 0,
#                                                 "y": 6,
#                                                 "w": 1640,
#                                                 "h": 918
#                                             },
#                                             {
#                                                 "x": 716,
#                                                 "y": 0,
#                                                 "w": 924,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 829,
#                                                 "y": 0,
#                                                 "w": 811,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 1178,
#                                                 "y": 0,
#                                                 "w": 462,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 0,
#                                                 "y": 0,
#                                                 "w": 1640,
#                                                 "h": 924
#                                             }
#                                         ]
#                                     }
#                                 }
#                             ],
#                             "user_mentions": [
#                                 {
#                                     "id_str": "1630090542758477824",
#                                     "name": "Paddas Finance",
#                                     "screen_name": "PaddasFinance",
#                                     "indices": [
#                                         3,
#                                         17
#                                     ]
#                                 },
#                                 {
#                                     "id_str": "1191702416971968512",
#                                     "name": "zkSync ∎",
#                                     "screen_name": "zksync",
#                                     "indices": [
#                                         32,
#                                         39
#                                     ]
#                                 }
#                             ],
#                             "urls": [],
#                             "hashtags": [],
#                             "symbols": []
#                         },
#                         "extended_entities": {
#                             "media": [
#                                 {
#                                     "display_url": "pic.twitter.com/JBE6ekCYuK",
#                                     "expanded_url": "https://twitter.com/PaddasFinance/status/1647010774638907392/photo/1",
#                                     "id_str": "1647010609387454464",
#                                     "indices": [
#                                         69,
#                                         92
#                                     ],
#                                     "media_key": "3_1647010609387454464",
#                                     "media_url_https": "https://pbs.twimg.com/media/FttbbEnWwAAxAIi.jpg",
#                                     "source_status_id_str": "1647010774638907392",
#                                     "source_user_id_str": "1630090542758477824",
#                                     "type": "photo",
#                                     "url": "https://t.co/JBE6ekCYuK",
#                                     "ext_media_availability": {
#                                         "status": "Available"
#                                     },
#                                     "sizes": {
#                                         "large": {
#                                             "h": 924,
#                                             "w": 1640,
#                                             "resize": "fit"
#                                         },
#                                         "medium": {
#                                             "h": 676,
#                                             "w": 1200,
#                                             "resize": "fit"
#                                         },
#                                         "small": {
#                                             "h": 383,
#                                             "w": 680,
#                                             "resize": "fit"
#                                         },
#                                         "thumb": {
#                                             "h": 150,
#                                             "w": 150,
#                                             "resize": "crop"
#                                         }
#                                     },
#                                     "original_info": {
#                                         "height": 924,
#                                         "width": 1640,
#                                         "focus_rects": [
#                                             {
#                                                 "x": 0,
#                                                 "y": 6,
#                                                 "w": 1640,
#                                                 "h": 918
#                                             },
#                                             {
#                                                 "x": 716,
#                                                 "y": 0,
#                                                 "w": 924,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 829,
#                                                 "y": 0,
#                                                 "w": 811,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 1178,
#                                                 "y": 0,
#                                                 "w": 462,
#                                                 "h": 924
#                                             },
#                                             {
#                                                 "x": 0,
#                                                 "y": 0,
#                                                 "w": 1640,
#                                                 "h": 924
#                                             }
#                                         ]
#                                     }
#                                 }
#                             ]
#                         },
#                         "favorite_count": 0,
#                         "favorited": 'False',
#                         "full_text": "RT @PaddasFinance: Comment your @zksync to summon something special. https://t.co/JBE6ekCYuK",
#                         "is_quote_status": 'False',
#                         "lang": "en",
#                         "possibly_sensitive": 'False',
#                         "possibly_sensitive_editable": 'true',
#                         "quote_count": 0,
#                         "reply_count": 0,
#                         "retweet_count": 67,
#                         "retweeted": 'False',
#                         "user_id_str": "1639665154991308800",
#                         "id_str": "1647010884370198528",
#                         "retweeted_status_result": {
#                             "result": {
#                                 "__typename": "Tweet",
#                                 "rest_id": "1647010774638907392",
#                                 "core": {
#                                     "user_results": {
#                                         "result": {
#                                             "__typename": "User",
#                                             "id": "VXNlcjoxNjMwMDkwNTQyNzU4NDc3ODI0",
#                                             "rest_id": "1630090542758477824",
#                                             "affiliates_highlighted_label": {},
#                                             "has_graduated_access": 'true',
#                                             "is_blue_verified": 'False',
#                                             "profile_image_shape": "Circle",
#                                             "legacy": {
#                                                 "can_dm": 'true',
#                                                 "can_media_tag": 'true',
#                                                 "created_at": "Mon Feb 27 06:20:48 +0000 2023",
#                                                 "default_profile": 'true',
#                                                 "default_profile_image": 'False',
#                                                 "description": "The first AutoStaking protocol on zkSync",
#                                                 "entities": {
#                                                     "description": {
#                                                         "urls": []
#                                                     },
#                                                     "url": {
#                                                         "urls": [
#                                                             {
#                                                                 "display_url": "paddas.finance",
#                                                                 "expanded_url": "http://paddas.finance",
#                                                                 "url": "https://t.co/ILb1gETYlM",
#                                                                 "indices": [
#                                                                     0,
#                                                                     23
#                                                                 ]
#                                                             }
#                                                         ]
#                                                     }
#                                                 },
#                                                 "fast_followers_count": 0,
#                                                 "favourites_count": 0,
#                                                 "followers_count": 609,
#                                                 "friends_count": 2,
#                                                 "has_custom_timelines": 'False',
#                                                 "is_translator": 'False',
#                                                 "listed_count": 9,
#                                                 "location": "",
#                                                 "media_count": 2,
#                                                 "name": "Paddas Finance",
#                                                 "normal_followers_count": 609,
#                                                 "pinned_tweet_ids_str": [
#                                                     "1646980761096970240"
#                                                 ],
#                                                 "possibly_sensitive": 'False',
#                                                 "profile_banner_url": "https://pbs.twimg.com/profile_banners/1630090542758477824/1681384539",
#                                                 "profile_image_url_https": "https://pbs.twimg.com/profile_images/1646474104130744320/Jen5T6WY_normal.jpg",
#                                                 "profile_interstitial_type": "",
#                                                 "screen_name": "PaddasFinance",
#                                                 "statuses_count": 6,
#                                                 "translator_type": "none",
#                                                 "url": "https://t.co/ILb1gETYlM",
#                                                 "verified": 'False',
#                                                 "want_retweets": 'False',
#                                                 "withheld_in_countries": []
#                                             }
#                                         }
#                                     }
#                                 },
#                                 "unmention_data": {},
#                                 "edit_control": {
#                                     "edit_tweet_ids": [
#                                         "1647010774638907392"
#                                     ],
#                                     "editable_until_msecs": "1681514743000",
#                                     "is_edit_eligible": 'true',
#                                     "edits_remaining": "5"
#                                 },
#                                 "edit_perspective": {
#                                     "favorited": 'False',
#                                     "retweeted": 'False'
#                                 },
#                                 "is_translatable": 'true',
#                                 "views": {
#                                     "count": "2774",
#                                     "state": "EnabledWithCount"
#                                 },
#                                 "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
#                                 "legacy": {
#                                     "bookmark_count": 0,
#                                     "bookmarked": 'False',
#                                     "created_at": "Fri Apr 14 22:55:43 +0000 2023",
#                                     "conversation_id_str": "1647010774638907392",
#                                     "display_text_range": [
#                                         0,
#                                         49
#                                     ],
#                                     "entities": {
#                                         "media": [
#                                             {
#                                                 "display_url": "pic.twitter.com/JBE6ekCYuK",
#                                                 "expanded_url": "https://twitter.com/PaddasFinance/status/1647010774638907392/photo/1",
#                                                 "id_str": "1647010609387454464",
#                                                 "indices": [
#                                                     50,
#                                                     73
#                                                 ],
#                                                 "media_url_https": "https://pbs.twimg.com/media/FttbbEnWwAAxAIi.jpg",
#                                                 "type": "photo",
#                                                 "url": "https://t.co/JBE6ekCYuK",
#                                                 "sizes": {
#                                                     "large": {
#                                                         "h": 924,
#                                                         "w": 1640,
#                                                         "resize": "fit"
#                                                     },
#                                                     "medium": {
#                                                         "h": 676,
#                                                         "w": 1200,
#                                                         "resize": "fit"
#                                                     },
#                                                     "small": {
#                                                         "h": 383,
#                                                         "w": 680,
#                                                         "resize": "fit"
#                                                     },
#                                                     "thumb": {
#                                                         "h": 150,
#                                                         "w": 150,
#                                                         "resize": "crop"
#                                                     }
#                                                 },
#                                                 "original_info": {
#                                                     "height": 924,
#                                                     "width": 1640,
#                                                     "focus_rects": [
#                                                         {
#                                                             "x": 0,
#                                                             "y": 6,
#                                                             "w": 1640,
#                                                             "h": 918
#                                                         },
#                                                         {
#                                                             "x": 716,
#                                                             "y": 0,
#                                                             "w": 924,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 829,
#                                                             "y": 0,
#                                                             "w": 811,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 1178,
#                                                             "y": 0,
#                                                             "w": 462,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 0,
#                                                             "y": 0,
#                                                             "w": 1640,
#                                                             "h": 924
#                                                         }
#                                                     ]
#                                                 }
#                                             }
#                                         ],
#                                         "user_mentions": [
#                                             {
#                                                 "id_str": "1191702416971968512",
#                                                 "name": "zkSync ∎",
#                                                 "screen_name": "zksync",
#                                                 "indices": [
#                                                     13,
#                                                     20
#                                                 ]
#                                             }
#                                         ],
#                                         "urls": [],
#                                         "hashtags": [],
#                                         "symbols": []
#                                     },
#                                     "extended_entities": {
#                                         "media": [
#                                             {
#                                                 "display_url": "pic.twitter.com/JBE6ekCYuK",
#                                                 "expanded_url": "https://twitter.com/PaddasFinance/status/1647010774638907392/photo/1",
#                                                 "id_str": "1647010609387454464",
#                                                 "indices": [
#                                                     50,
#                                                     73
#                                                 ],
#                                                 "media_key": "3_1647010609387454464",
#                                                 "media_url_https": "https://pbs.twimg.com/media/FttbbEnWwAAxAIi.jpg",
#                                                 "type": "photo",
#                                                 "url": "https://t.co/JBE6ekCYuK",
#                                                 "ext_media_availability": {
#                                                     "status": "Available"
#                                                 },
#                                                 "sizes": {
#                                                     "large": {
#                                                         "h": 924,
#                                                         "w": 1640,
#                                                         "resize": "fit"
#                                                     },
#                                                     "medium": {
#                                                         "h": 676,
#                                                         "w": 1200,
#                                                         "resize": "fit"
#                                                     },
#                                                     "small": {
#                                                         "h": 383,
#                                                         "w": 680,
#                                                         "resize": "fit"
#                                                     },
#                                                     "thumb": {
#                                                         "h": 150,
#                                                         "w": 150,
#                                                         "resize": "crop"
#                                                     }
#                                                 },
#                                                 "original_info": {
#                                                     "height": 924,
#                                                     "width": 1640,
#                                                     "focus_rects": [
#                                                         {
#                                                             "x": 0,
#                                                             "y": 6,
#                                                             "w": 1640,
#                                                             "h": 918
#                                                         },
#                                                         {
#                                                             "x": 716,
#                                                             "y": 0,
#                                                             "w": 924,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 829,
#                                                             "y": 0,
#                                                             "w": 811,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 1178,
#                                                             "y": 0,
#                                                             "w": 462,
#                                                             "h": 924
#                                                         },
#                                                         {
#                                                             "x": 0,
#                                                             "y": 0,
#                                                             "w": 1640,
#                                                             "h": 924
#                                                         }
#                                                     ]
#                                                 }
#                                             }
#                                         ]
#                                     },
#                                     "favorite_count": 100,
#                                     "favorited": 'False',
#                                     "full_text": "Comment your @zksync to summon something special. https://t.co/JBE6ekCYuK",
#                                     "is_quote_status": 'False',
#                                     "lang": "en",
#                                     "possibly_sensitive": 'False',
#                                     "possibly_sensitive_editable": 'true',
#                                     "quote_count": 0,
#                                     "reply_count": 107,
#                                     "retweet_count": 67,
#                                     "retweeted": 'False',
#                                     "user_id_str": "1630090542758477824",
#                                     "id_str": "1647010774638907392"
#                                 }
#                             }
#                         }
#                     }
#                 }
#             },
#             "tweetDisplayType": "Tweet"
#         },
#         "clientEventInfo": {
#             "component": "suggest_organic_list_tweet",
#             "element": "tweet",
#             "details": {
#                 "timelinesDetails": {
#                     "injectionType": "OrganicListTweet"
#                 }
#             }
#         }
#     }
# }
# b=jsonpath_ng.parse("$..created_at").find(only)[1].value
# print(b)
# from dateutil.tz import gettz
# # c=datetime.datetime.strptime('2023-04-23 12:12:53 CST','%Y-%m-%d %H:%M:%S %Z')
# # print(c)
# c=parser.parse('2023-04-23 12:12:53 UST')#.replace(tzinfo=gettz('Asia/Manila'))#.strftime('%Y-%m-%d %H:%M:%S %Z')
# print(c)
import speech_recognition as sr

import ffmpeg
from pydub import AudioSegment

import wave
import moviepy.editor as mpe


audioclip = mpe.AudioFileClip("file_0.oga")
audioclip.write_audiofile("output1.wav")

r = sr.Recognizer()
with sr.AudioFile('output.wav') as source:
    # 将语音文件读取为AudioData对象
    audio_data = r.record(source)
# 使用Google Speech Recognition进行识别
text = r.recognize_google(audio_data,language='zh-CN')

# 输出识别结果
print(text)
# d=datetime.datetime.strptime(str(c),'%Y-%m-%d %H:%M:%S %Z')
# print(d)
# print(time.strftime()time()strptime('%Y-%m-%d %H:%M:%S %Z')+'jjj')

# b=[2,3,4]['0']
# print(str(a))
# only=str(only)
# b=re.search(r"media_url_https.*?,",only).group()
# print(b[19:-2])
# c=''
# for i in b:
#     c+=i.replace(r'\n','\n')[13:-4]+'\n'
# print(c)

# # 添加多个成员
# list_id = 123456789  # 要添加成员的列表ID
# member_ids = [123, 456, 789]  # 要添加的成员ID列表
# api.add_list_members(list_id=list_id, user_id=member_ids)
# bot = telebot.TeleBot("6291256191:AAExAaaagpZgEAdBvhOMRN2JxlXr8om4qJA")
# bot.send_message(-1001982993052, 'nihao')
# a={'update_id': 852018352, 'channel_post': {'message_id': 9, 'author_signature': 'ylitchan @USTDAO',
#                                           'sender_chat': {'id': -1001982993052, 'title': 'day',
#                                                           'username': 'dayventure', 'type': 'channel'},
#                                           'chat': {'id': -1001982993052, 'title': 'day', 'username': 'dayventure',
#                                                    'type': 'channel'}, 'date': 1681612341, 'text': 'bot在哪'}}
# tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))

# from pybloom_live import ScalableBloomFilter
#
# # 创建 ScalableBloomFilter 对象
# sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
#
# # 插入数据
# sbfilter.add('foo')
# sbfilter.add('bar')
#
# # 判断数据是否存在
# print(sbfilter.add('3foo'))  # 输出 True
# print(sbfilter.add('3foo'))   # 输出 False
#
# import schedule
# import time
# import datetime
#
# def do_task():
#     # 这里是要执行的事务
#     print('执行事务')
#
# # 设置每天的 8 点执行任务
# schedule.every().day.at("15:47").do(do_task)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1800)
#
import slack

# SLACK_TOKEN = "xoxb-5109321480134-5119781200516-a9jKJpORzVF3up5IrAYjU2yb"
SLACK_TOKEN ='xoxp-5109321480134-5118401919620-5153089528371-48fc79253ec7046c7a4263436e3b43f5'
CHANNEL_ID = "C052ZB95CQP"

client = slack.WebClient(SLACK_TOKEN)
response = client.chat_postMessage(
    channel=CHANNEL_ID,
    text="<@U053SG7AC01> 你好啊",as_user=True

)
# import requests
# jsons={'_x_id': '14d3f3a0-1681660134.009',
# '_x_csid': 'pZHTOw8en3I',
# 'slack_route': 'T05379FE43Y',
# '_x_version_ts': 1681521451,
# '_x_gantry': True,
# 'fp': 'c7',
#     'token': 'xoxc-5109321480134-5118401919620-5115927274274-f4042446c2735027126e5864a7a9db38ab3236f758ef277a453df17452039846',
# 'channel': 'C052ZB95CQP',
# 'ts': '1681660134.xxxx82',
# 'type': 'message',
# 'xArgs': {"draft_id":"1fdaa4e0-5fd5-4c43-a8c0-b4a802685135"},
# 'unfurl': [],
# 'blocks': [{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"text","text":"得到的"}]}]}],
# 'draft_id': '1fdaa4e0-5fd5-4c43-a8c0-b4a802685135',
# 'include_channel_perm_error': True,
# 'client_msg_id': '21bca34e-a3bb-4456-a4f0-3822bfc1c69f',
# '_x_reason': 'webapp_message_send',
# '_x_mode': 'online',
# '_x_sonic': True}
# headers={'cookie':'_gcl_au=1.1.2012355713.1681573280; _gid=GA1.2.1297107388.1681573303; d=xoxd-rrB39IUbzY5ZcIVbU/N4fjUz7O1jFlYA7H00pGNQvRPmK+ucuS4peLJOexd7AyJR2iZ6zcakdeCJFbgREKOKxM7uGKb+wZqoOBxpTdbLcTjIXmecmenkgbD8X7qDU1T+jR9ahUxVPynO5Mobq45iDeRA9Wnpn2S4/F0dfVb4o67sN29I6jtp4zrg1A==; d-s=1681573350; lc=1681573350; b=.58d93f99d92b25ab0ab661a45c66a912; _ga=GA1.3.1247771316.1681573303; _gid=GA1.3.1297107388.1681573303; OptanonAlertBoxClosed=2023-04-15T16:07:27.790Z; __pdst=9ef40efd1c3e4089b4a4fcad4987a37d; _cs_c=1; _rdt_uuid=1681574848937.a2805b3a-9259-41e2-a9da-b95338a31e20; shown_ssb_redirect_page=1; ec=enQtNTExMDY3MzU0ODkwMi0zYTJjYjY5ZmZhZmY0OWYwZjU0YzYwZjM3ZDE1MDZjNmY0NDViMGVkY2UzZmU1NGQxYzU1MDRjMGNlNmZlMjU4; utm={"utm_source":"in-prod","utm_medium":"inprod-link_manage_apps-index-click"}; _ga=GA1.1.1247771316.1681573303; x=58d93f99d92b25ab0ab661a45c66a912.1681658376; _cs_mk_ga=0.4687026613902885_1681658381265; _cs_id=98598b25-11c5-ae5c-c6d1-7154641727a4.1681574848.2.1681659121.1681653578.1.1715738848839; _cs_s=19.0.0.1681660921802; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+16+2023+23:34:53+GMT+0800+(中国标准时间)&version=202211.1.0&isIABGlobal=False&hosts=&consentId=77073c00-f3ac-462f-9f0f-f77b168527e1&interactionCount=2&landingPath=NotLandingPage&groups=1:1,2:1,3:1,4:1&AwaitingReconsent=False&geolocation=SG;; PageCount=29; _ga_QTJQME5M5D=GS1.1.1681653578.2.1.1681659293.59.0.0',
#          'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
#          'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryNZPOGxCMA0JV8hwj'}
# a=requests.post('https://day-3eh6396.slack.com/api/chat.postMessage',data=jsons,headers=headers)
# a=requests.post('http://127.0.0.1:8000/newproject')
# print(a.json())
# regex = r'(cat)|(dog)'
# match = re.search(regex, 'hello ')

# a=['tweet_user'+'alpha_time'+'\n'+'tweet_text' for i in range(5)]
# print(a,type(a))
# print(time.strftime("%Y-%m-%d",time.localtime(1681920736)))
# import telebot
# import osdata.list.tweets_timeline.timeline.instructions[0].entries[0].content.itemContent.tweet_results.result.legacy.created_at

# print(os.getenv('openai'))
# # a={i for i in [2,3,2,4,5,2,3,]}
# # print(a)
# # # alpha_time=re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+|中国标准时间', '2023-04-18 20:55:48 launching中国标准时间\nsale')
# # # print(alpha_time.group().replace('-','\-'))
# bot = telebot.TeleBot("6074723596:AAEeU2OjyTYVwf0fsLN854qe6X92prsEli8")
# # # # # entities = [
# # # # #     MessageEntity(MessageEntity.MENTION, offset=10, length=8, username="example_user"),
# # # # #     MessageEntity(MessageEntity.HASHTAG, offset=20, length=10, hashtag="exampletag"),
# # # # #     MessageEntity(MessageEntity.URL, offset=30, length=20, url="https://example.com/")
# # # # # ]
# #
# bot.send_message(-1001982993052,'[SoluneaDex](https://twitter\.com/SoluneaDex) @[2023\-04\-18 21:19:35 中国标准时间](https://twitter\.com/killall1234/status/1648316761274724352) wo[fhaoidh](oasno)')
# # from jsonpath_ng import parse
# #
# # data = {
# #     "store": {
# #         "book": {
# #             "category": "reference",
# #             "author": "Nigel Rees",
# #             "title": "Sayings of the Century",
# #             "price": 8.95
# #         }
# #     }
# # }
# # a=parse('$..title').find(data)[:2][-1].value
# # print(a)