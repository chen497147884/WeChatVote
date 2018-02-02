#! /usr/bin/env python  
#coding=utf-8  
import urllib2  
import urllib  
import cookielib  
  
def login():  
    email = raw_input("请输入用户名:")  
    pwd = raw_input("请输入密码:")  
    data={"email":email,"password":pwd}  #登陆用户名和密码  
    post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式  
    cj=cookielib.CookieJar()   #获取cookiejar实例  
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
    #自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）  
    headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}  
    website = raw_input('请输入网址:')  
    req=urllib2.Request(website,post_data,headers)  
    content=opener.open(req)  
    print content.read()    #linux下没有gbk编码，只有utf-8编码  
  
if __name__ == '__main__':  
    login()  