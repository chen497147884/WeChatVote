'''
    2017��6��1��22:53:56
    ���������ء�����ˢƱ���
    ��Ҫ�����ڸ��Լ�����ˢƱ�õ�
'''
import requests
import json
import time
import re

# ����ͷ��Ϣ
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.dingnf.com',
    'Origin': 'http://www.dingnf.com',
    'Referer': 'http://www.dingnf.com/active/wxws_s',
    'User-Agent': 'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# post����ַ
url = "http://www.dingnf.com/active/wxws_t"
params = {'ids': ['22', '22', '22']}


def WriteIPadress():
    all_url = []  # �洢IP��ַ������
    # ����IP����ַ
    url = "http://api.xicidaili.com/free2016.txt"
    r = requests.get(url=url)
    all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
    with open("D:\\code\\python\\new\\Brush ticket\\IP.txt", 'w') as f:
        for i in all_url:
            f.write(i)
            f.write('\n')
    return all_url

# ������
count = 0
while count < 4000:
    all_url = WriteIPadress()
    for i in all_url:
        proxies = {"http": i}
        try:
            r = requests.post(url=url, data=params,
                              headers=headers, proxies=proxies, timeout=10)
            if(r.json()['flag'] == True):
                count += 1
                print("�ɹ�ͶƱ%d�Σ�" % (count))
            print(r.json())
        except Exception as reason:
            print("����ԭ���ǣ�", reason)