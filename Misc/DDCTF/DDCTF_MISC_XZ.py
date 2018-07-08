import base64

flag=""
a='d4 e8 e1 f4 a0 f7 e1 f3 a0 e6 e1 f3 f4 a1 a0 d4 e8 e5 a0 e6 ec e1 e7 a0 e9 f3 ba a0 c4 c4 c3 d4 c6 fb b7 b9 b8 e4 b5 b5 e4 e2 b7 b6 b5 b5 b2 e1 b9 b2 b2 e4 b0 b0 e4 b7 b7 b5 e5 b3 b3 b1 b1 b9 b0 b7 fd '
s=a.split();
for i in xrange(128):
    flag=""
    for x in s :
        flag+=chr((int(x,16)+i+128*5)% 128)
    print flag