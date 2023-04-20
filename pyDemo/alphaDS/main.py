import multiprocessing
from scrapy import cmdline
if __name__ == "__main__":
    while True:
        process = multiprocessing.Process(target=cmdline.execute,args=[["scrapy", "crawl", "alpha","--nolog"]])
        process.start()
        process.join()