#!/usr/bin/env python
# coding=utf-8
from pwn import *
flag="";
while 1:
	p=remote("10.21.107.223",8989)
	print p.recvuntil(">")
	p.sendline(flag.ljust(28,"0"))
	data=p.recvuntil("~")
	z= ord(data[23:24])
	print z
	ans=ord("0")+256-z
	flag+=chr(ans)
	print flag
