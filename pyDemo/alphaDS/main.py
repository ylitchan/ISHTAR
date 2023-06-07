import time
import schedule
import subprocess


def work():
    subprocess.Popen('scrapy crawl alpha --nolog')
    print('开始子进程', time.strftime('%Y-%m-%d %H:%M:%S %Z %A'))


schedule.every(3610).seconds.do(work)
if __name__ == "__main__":
    work()
    while True:
        schedule.run_pending()
