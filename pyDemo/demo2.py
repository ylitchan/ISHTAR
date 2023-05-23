import datetime
import time
import requests
from dateutil import parser

a = datetime.datetime.now()
a=requests.post('https://alpha-admin.ipfszj.com/api/admin/alpha/caller/add', headers={
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc1JlZnJlc2giOmZhbHNlLCJyb2xlSWRzIjpbIjEwIl0sInVzZXJuYW1lIjoiYXV0b2FkZCIsInVzZXJJZCI6NCwicGFzc3dvcmRWZXJzaW9uIjoxLCJpYXQiOjE2ODQ2NzQ3NTUsImV4cCI6MTcxNjIxMDc1NX0.JjT_rr-Iu1l_i1hnvm_HzkwHZJnwMU8XEN280G3XHbo'},
              json={'tweetId': '4534534', 'tweetUser': 'ust',
                    'tweetAlpha': 'dao', 'tweetText': 'launch',
                    'tweetMedia': '', 'tweetAi': 'nice',
                    'tweetTag': 'launch', 'alphaDatetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z'),
                    'userThumb': 'https', 'alphaThumb': 'http',
                    'tweetTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')})

print(a)
