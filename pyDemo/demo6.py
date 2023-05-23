import time
start = time.perf_counter()
time.sleep(3)
end = time.perf_counter()
from dateutil import parser
a=parser.parse('2023-05-20 11:15:03 CST')
print(a.strftime('%Y-%m-%d %H:%M:%S %Z'))