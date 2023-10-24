import time
import requests
from pprint import pprint
from tqdm import tqdm

def get_response_time(url):
    start_time = time.time()  # 记录开始时间
    response = requests.get(url, timeout=3)  # 发送请求
    end_time = time.time()  # 记录结束时间
    response_time = end_time - start_time  # 计算响应时间
    return response_time

# view https://zhuanlan.zhihu.com/p/104285769
dns = dict(
    tecent = ['119.29.29.29', '182.254.118.118'],
    aliyun = ['223.5.5.5', '223.6.6.6'],
    baidu = ['180.76.76.76'],
    dsn114 = ['114.114.114.114', '114.114.115.115'],
    cnnic = ['1.2.4.8', '210.2.4.8'],
    google = ['8.8.8.8', '8.8.4.4'],
    dns360 = ['101.226.4.6', '123.125.81.6', '101.226.4.6', '101.226.4.6']
    )


results = {}
for key in tqdm(dns):
    for ip in dns[key]:
        url = f'http://{ip}'
        try:
            response_time = get_response_time(url)
            results[ip] = response_time
        except:
            results[ip] = 100

        print(ip, 'timeout' if results[ip]==100 else results[ip])
results = sorted(results.items(), key=lambda x: x[1])
pprint(results)
