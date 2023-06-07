import datetime
import time
import requests
from dateutil import parser

a = datetime.datetime.now()
session = requests.Session()
c = session.post('http://ishtar.freehk.svipss.top/getmsg', json={'user_phone': '13376982550'},timeout=10)
print(c.json())
