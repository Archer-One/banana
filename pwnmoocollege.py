import requests

url='http://student.zjedu2.moocollege.com/nodeapi/3.0.1/student/course/uploadLearnRate'

Cookie={
'NOISSESUDEJZXJ':'s%3AXEwRoxI7XJP7xNvAG7MxEyHbT_N_11l5.Yw8KLJLuEk5CPVfGAJMt65cSVfMc2kzdtmlOmUnZGgA',
'token-student-zjedu':'%2255d6257a-4d5b-4ae2-9db1-1c37c73f218b%22',
'realname-student-zjedu':'%22%E6%A2%85%E7%BF%94%22',
'avatar-student-zjedu':'null',
'ccPlayer-MediaType-zjedu':'%22html5%22'
}
data={
    'unitId':'30062486',
    'courseId':'30001937',
    'playPosition':'1'
}
for x in range(1,1000,5):
    data['playPosition']=str(x)
    res=requests.post(url=url,cookies=Cookie,data=data)
    print str(x)+"/1000";
