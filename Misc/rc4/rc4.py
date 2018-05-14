key="RC4"
C=""
s=[];
t=[]
print "==============part1 start============="
for x in xrange(256):
    s.append(x);
    t.append(key[x%len(key)])
print s;
print t;
print "==============part2 start============="

j=0;
for x in xrange(256):
    j=(j+s[x]+ord(t[x]))%256;
    tmp=s[j]
    s[j]=s[x];
    s[x]=tmp
print s
print "==============part3 start============="

i=0
j=0;
k=[1,2,3,4,5,6,7,8,9]
print len(s)
print len(k)
for x in xrange(9):
    i=i+1
    i=i%256
    j=j+s[i]
    j=j%256
    tmp=s[j]
    s[j]=s[i];
    s[i]=tmp
    tmp+=s[i];
    t=tmp%256
    k[x]=s[t]
print k
raw=['1','2','3','4','5','6','7','8','9']
ans=""
for x in xrange(9):
    ans+=chr(ord(raw[x])^k[x]);
import base64
print base64.b64encode(ans)