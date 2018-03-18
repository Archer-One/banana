#encoding=utf8
url='https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryright.cgi?uin=*********&rd=0.0104272023165205&ver=1&fupdate=1&g_tk=1120121934&qzonetoken=********'
cookie={
#此处填cookie
}
import requests
import re
zz='https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?uin=****&hostUin=****&num=10&start={}&hostword=0&essence=1&r=0.10576292772713614&iNotice=0&inCharset=utf-8&outCharset=utf-8&format=jsonp&ref=qzone&g_tk=1120121934&qzonetoken=****'
fp=open("out.txt",'a')
for i in xrange(1,500):
    res = requests.get(url=zz.format(str(i)+'0'), cookies=cookie)
    mat = r'htmlConten.*'
    t = re.findall(mat, str(res.content))
    for x in t:
        print x[14:-2]
        fp.write(x+"\n")