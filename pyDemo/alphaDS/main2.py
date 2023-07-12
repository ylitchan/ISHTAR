import time
import schedule
import subprocess
from scrapy import cmdline

# cmdline.execute(['scrapy', 'crawl', 'newAlpha', '--nolog'])


def work():
    # cmdline.execute(['scrapy', 'crawl', 'alpha', '--nolog'])
    subprocess.Popen('scrapy crawl newAlpha ')
    print('开始子进程', time.strftime('%Y-%m-%d %H:%M:%S %Z %A'))


schedule.every(1810).seconds.do(work)
if __name__ == "__main__":
    work()
    while True:
        schedule.run_pending()
