'''
with open("sand.txt", "r") as f:
	for i in range(20):
         print 1;
'''
def lcm(m,n):
    if (m%n==0):
            return n;
    return lcm(n,m%n)

def gbs(m,n):
    return m*n/lcm(m,n);
re=[222,203,33,135,203,62,227,82,239,82,11,220,74,92,8,308,195,165,87,4]
holes = [257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373]
f=open("sand.txt", "w")
n=222
i=0;
now=1;
for x in holes:

    print "{}%{}=={} if not + {}".format(n,x,re[i],now)
    while n%x!=re[i]:
        n+=now
    i+=1;
    print "now=gbs({},{})".format(now,holes[i-1])
    now = gbs(now, holes[i-1])
print hex(n)

t=n
for i in range(20):
        sand = t % holes[i]
        print sand

