import random
import time

import requests
from scrapy import cmdline
import threading
def worker():
    import tg2tweet
thread=threading.Thread(target=worker)
thread.daemon=True
thread.start()
cmdline.execute(["scrapy", "crawl", "alpha","-s", "LOG_FILE=scrapy.log"])

