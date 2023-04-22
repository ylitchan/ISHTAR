import requests
import tweepy

#
#
# def add_member(user_id):
#     var = {"variables": {"listId": "1639838455760035840", "userId": user_id},
#            "features": {"blue_business_profile_image_shape_enabled": False,
#                         "responsive_web_graphql_exclude_directive_enabled": True, "verified_phone_label_enabled": False,
#                         "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
#                         "responsive_web_graphql_timeline_navigation_enabled": True}}
#     headers ={'cookie': 'des_opt_in=Y; _gcl_au=1.1.116267149.1676257589; g_state={"i_l":4,"i_p":1681369247236}; '
#                         '_gid=GA1.2.445506973.1679573193; _ga_BYKEBDM7DS=GS1.1.1679899771.1.1.1679899844.0.0.0; '
#                         'mbox=PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1743168876|session'
#                         '#3739bd11cd84406f8d3366750345558f#1679925936; _ga=GA1.2.1915858432.1679573193; '
#                         '_ga_34PHSZMC42=GS1.1.1679926617.9.0.1679926617.0.0.0; guest_id_ads=v1:167998590896091627; '
#                         'guest_id_marketing=v1:167998590896091627; gt=1640605928444809216; '
#                         'guest_id=v1:167998590896091627; '
#                         '_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo'
#                         '%0ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFau9iaHAToMY3NyZl9p'
#                         '%0AZCIlNzI4ZjBmNDhhZjBhNmZjZjczZjJiYmI5MWRlNDhjOGU6B2lkIiU5NDEx'
#                         '%0AZDJkMDdlZTk1YTYzMTYxNDM4NDFlODA2ZGNhMg%3D%3D--ba14a990d9fc97c4e20f7419e6f58ca40d964ff6; '
#                         'kdt=pWxhXrYLndl6kFnt3TwRYuUHorLwD0qgQgh1EMmY; '
#                         'auth_token=9a544b8e5f655464d8e9b5c5da6ebb699a174c68; '
#                         'ct0=07e7120541046fff57dac4d71488037d9005f838efcb058e31cc3148157323836afbc8dd8e6929a310a26809cc13e87b93405b524af8552f33ebcbabd53e5a456ecefc7aea71c8b31b5490e0a288e5f9; lang=zh-cn; twid=u=1568898000654680064; att=1-f05kvL4WYIwHMqJNVA2AOkAARB1B4w4YTuyZbrSE; personalization_id="v1_TmHvZLb91IxgNxuW3Fi3pg=="',
#         'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#         'x-csrf-token': '07e7120541046fff57dac4d71488037d9005f838efcb058e31cc3148157323836afbc8dd8e6929a310a26809cc13e87b93405b524af8552f33ebcbabd53e5a456ecefc7aea71c8b31b5490e0a288e5f9',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
#     res=requests.post('https://twitter.com/i/api/graphql/AII7W0kWK7nz89PKR5lAeg/ListAddMember', json=var,
#                       headers=headers)
#     print(res)
# add_member(939580637219975168)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPEGjQEAAAAAREb6WuXu7rNwm8ChnkpJoSJmSkw%3DXgtd6IlBg9SyrAcVhTOVucCrYL4OGfSjjCmMbfM8mFTi3CqUcL"
client = tweepy.Client(consumer_key='m7zm88QlDV2bM7CULixM02lxR',consumer_secret='xESd9f3fZEg6HBsqvAZqTrU4FZhVw5Q3hHH8wzJGgghnYFExnb')
# a=client.get_me()
# print(a)
res = client.get_user(id=1254538550906728448, user_fields=["profile_image_url"])
print(res)