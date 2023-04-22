from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def newproject(request):
    lookup_fields = request.data.get('lookup_fields','')
    order_fields = request.data.get('order_fields','')

    # 校验lookup_fields和order_fields
    if lookup_fields:
        pass
    if order_fields:
        pass


    return Response({"username": "@ust_dao","FollowedToday":1,"Followers":1,"Bio":"UST DAO 牛逼","Created":"04/22/2023","DiscoveryTime":"2023-04-22"})


@api_view(['POST'])
def launching(request):
    lookup_fields = request.data.get('lookup_fields','')
    order_fields = request.data.get('order_fields','')

    # 校验lookup_fields和order_fields
    if lookup_fields:
        pass
    if order_fields:
        pass


    return Response({"tweet_user": "ust_dao","tweet_alpha":" @dao_ust","tweet_text":"UST DAO 牛逼plus","user_thumb":"https://api.cyfan.top/acg","tweet_media":"https://pbs.twimg.com/media/FuKsFCUaMAAK0wy.jpg","alpha_time":"2023-04-23","tweet_time":"2023-04-22"})