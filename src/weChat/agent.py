'''
    2017��6��1��15:15:15
    ��ȡ����IP��վ��API������ô���IP
    1. �������������API�ӿ�
    2. ������ݣ�����������ʽ��ȡ�ؼ�����
    3. ���б���ؼ�����
'''
import requests
import re



all_url = [] # �洢IP��ַ������

# ����IP����ַ
url = "http://api.xicidaili.com/free2016.txt"
r = requests.get(url=url)
all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+",r.text)

with open("resource\\ip.txt",'w') as f:
    for i in all_url:
        f.write(i)
        f.write('\n')

for i in all_url:
    print(i)