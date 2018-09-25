
callme:     file format elf64-x86-64


Disassembly of section .init:

00000000004017c0 <_init>:
  4017c0:	48 83 ec 08          	sub    $0x8,%rsp
  4017c4:	48 8b 05 2d 08 20 00 	mov    0x20082d(%rip),%rax        # 601ff8 <_DYNAMIC+0x1f0>
  4017cb:	48 85 c0             	test   %rax,%rax
  4017ce:	74 05                	je     4017d5 <_init+0x15>
  4017d0:	e8 bb 00 00 00       	callq  401890 <exit@plt+0x10>
  4017d5:	48 83 c4 08          	add    $0x8,%rsp
  4017d9:	c3                   	retq   

Disassembly of section .plt:

00000000004017e0 <puts@plt-0x10>:
  4017e0:	ff 35 22 08 20 00    	pushq  0x200822(%rip)        # 602008 <_GLOBAL_OFFSET_TABLE_+0x8>
  4017e6:	ff 25 24 08 20 00    	jmpq   *0x200824(%rip)        # 602010 <_GLOBAL_OFFSET_TABLE_+0x10>
  4017ec:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004017f0 <puts@plt>:
  4017f0:	ff 25 22 08 20 00    	jmpq   *0x200822(%rip)        # 602018 <_GLOBAL_OFFSET_TABLE_+0x18>
  4017f6:	68 00 00 00 00       	pushq  $0x0
  4017fb:	e9 e0 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401800 <printf@plt>:
  401800:	ff 25 1a 08 20 00    	jmpq   *0x20081a(%rip)        # 602020 <_GLOBAL_OFFSET_TABLE_+0x20>
  401806:	68 01 00 00 00       	pushq  $0x1
  40180b:	e9 d0 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401810 <callme_three@plt>:
  401810:	ff 25 12 08 20 00    	jmpq   *0x200812(%rip)        # 602028 <_GLOBAL_OFFSET_TABLE_+0x28>
  401816:	68 02 00 00 00       	pushq  $0x2
  40181b:	e9 c0 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401820 <memset@plt>:
  401820:	ff 25 0a 08 20 00    	jmpq   *0x20080a(%rip)        # 602030 <_GLOBAL_OFFSET_TABLE_+0x30>
  401826:	68 03 00 00 00       	pushq  $0x3
  40182b:	e9 b0 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401830 <__libc_start_main@plt>:
  401830:	ff 25 02 08 20 00    	jmpq   *0x200802(%rip)        # 602038 <_GLOBAL_OFFSET_TABLE_+0x38>
  401836:	68 04 00 00 00       	pushq  $0x4
  40183b:	e9 a0 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401840 <fgets@plt>:
  401840:	ff 25 fa 07 20 00    	jmpq   *0x2007fa(%rip)        # 602040 <_GLOBAL_OFFSET_TABLE_+0x40>
  401846:	68 05 00 00 00       	pushq  $0x5
  40184b:	e9 90 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401850 <callme_one@plt>:
  401850:	ff 25 f2 07 20 00    	jmpq   *0x2007f2(%rip)        # 602048 <_GLOBAL_OFFSET_TABLE_+0x48>
  401856:	68 06 00 00 00       	pushq  $0x6
  40185b:	e9 80 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401860 <setvbuf@plt>:
  401860:	ff 25 ea 07 20 00    	jmpq   *0x2007ea(%rip)        # 602050 <_GLOBAL_OFFSET_TABLE_+0x50>
  401866:	68 07 00 00 00       	pushq  $0x7
  40186b:	e9 70 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401870 <callme_two@plt>:
  401870:	ff 25 e2 07 20 00    	jmpq   *0x2007e2(%rip)        # 602058 <_GLOBAL_OFFSET_TABLE_+0x58>
  401876:	68 08 00 00 00       	pushq  $0x8
  40187b:	e9 60 ff ff ff       	jmpq   4017e0 <_init+0x20>

0000000000401880 <exit@plt>:
  401880:	ff 25 da 07 20 00    	jmpq   *0x2007da(%rip)        # 602060 <_GLOBAL_OFFSET_TABLE_+0x60>
  401886:	68 09 00 00 00       	pushq  $0x9
  40188b:	e9 50 ff ff ff       	jmpq   4017e0 <_init+0x20>

Disassembly of section .plt.got:

0000000000401890 <.plt.got>:
  401890:	ff 25 62 07 20 00    	jmpq   *0x200762(%rip)        # 601ff8 <_DYNAMIC+0x1f0>
  401896:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000000004018a0 <_start>:
  4018a0:	31 ed                	xor    %ebp,%ebp
  4018a2:	49 89 d1             	mov    %rdx,%r9
  4018a5:	5e                   	pop    %rsi
  4018a6:	48 89 e2             	mov    %rsp,%rdx
  4018a9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4018ad:	50                   	push   %rax
  4018ae:	54                   	push   %rsp
  4018af:	49 c7 c0 30 1b 40 00 	mov    $0x401b30,%r8
  4018b6:	48 c7 c1 c0 1a 40 00 	mov    $0x401ac0,%rcx
  4018bd:	48 c7 c7 96 19 40 00 	mov    $0x401996,%rdi
  4018c4:	e8 67 ff ff ff       	callq  401830 <__libc_start_main@plt>
  4018c9:	f4                   	hlt    
  4018ca:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

00000000004018d0 <deregister_tm_clones>:
  4018d0:	b8 7f 20 60 00       	mov    $0x60207f,%eax
  4018d5:	55                   	push   %rbp
  4018d6:	48 2d 78 20 60 00    	sub    $0x602078,%rax
  4018dc:	48 83 f8 0e          	cmp    $0xe,%rax
  4018e0:	48 89 e5             	mov    %rsp,%rbp
  4018e3:	76 1b                	jbe    401900 <deregister_tm_clones+0x30>
  4018e5:	b8 00 00 00 00       	mov    $0x0,%eax
  4018ea:	48 85 c0             	test   %rax,%rax
  4018ed:	74 11                	je     401900 <deregister_tm_clones+0x30>
  4018ef:	5d                   	pop    %rbp
  4018f0:	bf 78 20 60 00       	mov    $0x602078,%edi
  4018f5:	ff e0                	jmpq   *%rax
  4018f7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  4018fe:	00 00 
  401900:	5d                   	pop    %rbp
  401901:	c3                   	retq   
  401902:	0f 1f 40 00          	nopl   0x0(%rax)
  401906:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40190d:	00 00 00 

0000000000401910 <register_tm_clones>:
  401910:	be 78 20 60 00       	mov    $0x602078,%esi
  401915:	55                   	push   %rbp
  401916:	48 81 ee 78 20 60 00 	sub    $0x602078,%rsi
  40191d:	48 c1 fe 03          	sar    $0x3,%rsi
  401921:	48 89 e5             	mov    %rsp,%rbp
  401924:	48 89 f0             	mov    %rsi,%rax
  401927:	48 c1 e8 3f          	shr    $0x3f,%rax
  40192b:	48 01 c6             	add    %rax,%rsi
  40192e:	48 d1 fe             	sar    %rsi
  401931:	74 15                	je     401948 <register_tm_clones+0x38>
  401933:	b8 00 00 00 00       	mov    $0x0,%eax
  401938:	48 85 c0             	test   %rax,%rax
  40193b:	74 0b                	je     401948 <register_tm_clones+0x38>
  40193d:	5d                   	pop    %rbp
  40193e:	bf 78 20 60 00       	mov    $0x602078,%edi
  401943:	ff e0                	jmpq   *%rax
  401945:	0f 1f 00             	nopl   (%rax)
  401948:	5d                   	pop    %rbp
  401949:	c3                   	retq   
  40194a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000401950 <__do_global_dtors_aux>:
  401950:	80 3d 51 07 20 00 00 	cmpb   $0x0,0x200751(%rip)        # 6020a8 <completed.7585>
  401957:	75 11                	jne    40196a <__do_global_dtors_aux+0x1a>
  401959:	55                   	push   %rbp
  40195a:	48 89 e5             	mov    %rsp,%rbp
  40195d:	e8 6e ff ff ff       	callq  4018d0 <deregister_tm_clones>
  401962:	5d                   	pop    %rbp
  401963:	c6 05 3e 07 20 00 01 	movb   $0x1,0x20073e(%rip)        # 6020a8 <completed.7585>
  40196a:	f3 c3                	repz retq 
  40196c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401970 <frame_dummy>:
  401970:	bf 00 1e 60 00       	mov    $0x601e00,%edi
  401975:	48 83 3f 00          	cmpq   $0x0,(%rdi)
  401979:	75 05                	jne    401980 <frame_dummy+0x10>
  40197b:	eb 93                	jmp    401910 <register_tm_clones>
  40197d:	0f 1f 00             	nopl   (%rax)
  401980:	b8 00 00 00 00       	mov    $0x0,%eax
  401985:	48 85 c0             	test   %rax,%rax
  401988:	74 f1                	je     40197b <frame_dummy+0xb>
  40198a:	55                   	push   %rbp
  40198b:	48 89 e5             	mov    %rsp,%rbp
  40198e:	ff d0                	callq  *%rax
  401990:	5d                   	pop    %rbp
  401991:	e9 7a ff ff ff       	jmpq   401910 <register_tm_clones>

0000000000401996 <main>:
  401996:	55                   	push   %rbp
  401997:	48 89 e5             	mov    %rsp,%rbp
  40199a:	48 8b 05 df 06 20 00 	mov    0x2006df(%rip),%rax        # 602080 <stdout@@GLIBC_2.2.5>
  4019a1:	b9 00 00 00 00       	mov    $0x0,%ecx
  4019a6:	ba 02 00 00 00       	mov    $0x2,%edx
  4019ab:	be 00 00 00 00       	mov    $0x0,%esi
  4019b0:	48 89 c7             	mov    %rax,%rdi
  4019b3:	e8 a8 fe ff ff       	callq  401860 <setvbuf@plt>
  4019b8:	48 8b 05 e1 06 20 00 	mov    0x2006e1(%rip),%rax        # 6020a0 <stderr@@GLIBC_2.2.5>
  4019bf:	b9 00 00 00 00       	mov    $0x0,%ecx
  4019c4:	ba 02 00 00 00       	mov    $0x2,%edx
  4019c9:	be 00 00 00 00       	mov    $0x0,%esi
  4019ce:	48 89 c7             	mov    %rax,%rdi
  4019d1:	e8 8a fe ff ff       	callq  401860 <setvbuf@plt>
  4019d6:	bf 48 1b 40 00       	mov    $0x401b48,%edi
  4019db:	e8 10 fe ff ff       	callq  4017f0 <puts@plt>
  4019e0:	bf 5f 1b 40 00       	mov    $0x401b5f,%edi
  4019e5:	e8 06 fe ff ff       	callq  4017f0 <puts@plt>
  4019ea:	b8 00 00 00 00       	mov    $0x0,%eax
  4019ef:	e8 11 00 00 00       	callq  401a05 <pwnme>
  4019f4:	bf 67 1b 40 00       	mov    $0x401b67,%edi
  4019f9:	e8 f2 fd ff ff       	callq  4017f0 <puts@plt>
  4019fe:	b8 00 00 00 00       	mov    $0x0,%eax
  401a03:	5d                   	pop    %rbp
  401a04:	c3                   	retq   

0000000000401a05 <pwnme>:
  401a05:	55                   	push   %rbp
  401a06:	48 89 e5             	mov    %rsp,%rbp
  401a09:	48 83 ec 20          	sub    $0x20,%rsp
  401a0d:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
  401a11:	ba 20 00 00 00       	mov    $0x20,%edx
  401a16:	be 00 00 00 00       	mov    $0x0,%esi
  401a1b:	48 89 c7             	mov    %rax,%rdi
  401a1e:	e8 fd fd ff ff       	callq  401820 <memset@plt>
  401a23:	bf 70 1b 40 00       	mov    $0x401b70,%edi
  401a28:	e8 c3 fd ff ff       	callq  4017f0 <puts@plt>
  401a2d:	bf 92 1b 40 00       	mov    $0x401b92,%edi
  401a32:	b8 00 00 00 00       	mov    $0x0,%eax
  401a37:	e8 c4 fd ff ff       	callq  401800 <printf@plt>
  401a3c:	48 8b 15 4d 06 20 00 	mov    0x20064d(%rip),%rdx        # 602090 <stdin@@GLIBC_2.2.5>
  401a43:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
  401a47:	be 00 01 00 00       	mov    $0x100,%esi
  401a4c:	48 89 c7             	mov    %rax,%rdi
  401a4f:	e8 ec fd ff ff       	callq  401840 <fgets@plt>
  401a54:	90                   	nop
  401a55:	c9                   	leaveq 
  401a56:	c3                   	retq   

0000000000401a57 <usefulFunction>:
  401a57:	55                   	push   %rbp
  401a58:	48 89 e5             	mov    %rsp,%rbp
  401a5b:	ba 06 00 00 00       	mov    $0x6,%edx
  401a60:	be 05 00 00 00       	mov    $0x5,%esi
  401a65:	bf 04 00 00 00       	mov    $0x4,%edi
  401a6a:	e8 a1 fd ff ff       	callq  401810 <callme_three@plt>
  401a6f:	ba 06 00 00 00       	mov    $0x6,%edx
  401a74:	be 05 00 00 00       	mov    $0x5,%esi
  401a79:	bf 04 00 00 00       	mov    $0x4,%edi
  401a7e:	e8 ed fd ff ff       	callq  401870 <callme_two@plt>
  401a83:	ba 06 00 00 00       	mov    $0x6,%edx
  401a88:	be 05 00 00 00       	mov    $0x5,%esi
  401a8d:	bf 04 00 00 00       	mov    $0x4,%edi
  401a92:	e8 b9 fd ff ff       	callq  401850 <callme_one@plt>
  401a97:	bf 01 00 00 00       	mov    $0x1,%edi
  401a9c:	e8 df fd ff ff       	callq  401880 <exit@plt>
  401aa1:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  401aa8:	00 00 00 
  401aab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000401ab0 <usefulGadgets>:
  401ab0:	5f                   	pop    %rdi
  401ab1:	5e                   	pop    %rsi
  401ab2:	5a                   	pop    %rdx
  401ab3:	c3                   	retq   
  401ab4:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  401abb:	00 00 00 
  401abe:	66 90                	xchg   %ax,%ax

0000000000401ac0 <__libc_csu_init>:
  401ac0:	41 57                	push   %r15
  401ac2:	41 56                	push   %r14
  401ac4:	41 89 ff             	mov    %edi,%r15d
  401ac7:	41 55                	push   %r13
  401ac9:	41 54                	push   %r12
  401acb:	4c 8d 25 1e 03 20 00 	lea    0x20031e(%rip),%r12        # 601df0 <__frame_dummy_init_array_entry>
  401ad2:	55                   	push   %rbp
  401ad3:	48 8d 2d 1e 03 20 00 	lea    0x20031e(%rip),%rbp        # 601df8 <__init_array_end>
  401ada:	53                   	push   %rbx
  401adb:	49 89 f6             	mov    %rsi,%r14
  401ade:	49 89 d5             	mov    %rdx,%r13
  401ae1:	4c 29 e5             	sub    %r12,%rbp
  401ae4:	48 83 ec 08          	sub    $0x8,%rsp
  401ae8:	48 c1 fd 03          	sar    $0x3,%rbp
  401aec:	e8 cf fc ff ff       	callq  4017c0 <_init>
  401af1:	48 85 ed             	test   %rbp,%rbp
  401af4:	74 20                	je     401b16 <__libc_csu_init+0x56>
  401af6:	31 db                	xor    %ebx,%ebx
  401af8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  401aff:	00 
  401b00:	4c 89 ea             	mov    %r13,%rdx
  401b03:	4c 89 f6             	mov    %r14,%rsi
  401b06:	44 89 ff             	mov    %r15d,%edi
  401b09:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  401b0d:	48 83 c3 01          	add    $0x1,%rbx
  401b11:	48 39 eb             	cmp    %rbp,%rbx
  401b14:	75 ea                	jne    401b00 <__libc_csu_init+0x40>
  401b16:	48 83 c4 08          	add    $0x8,%rsp
  401b1a:	5b                   	pop    %rbx
  401b1b:	5d                   	pop    %rbp
  401b1c:	41 5c                	pop    %r12
  401b1e:	41 5d                	pop    %r13
  401b20:	41 5e                	pop    %r14
  401b22:	41 5f                	pop    %r15
  401b24:	c3                   	retq   
  401b25:	90                   	nop
  401b26:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  401b2d:	00 00 00 

0000000000401b30 <__libc_csu_fini>:
  401b30:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000401b34 <_fini>:
  401b34:	48 83 ec 08          	sub    $0x8,%rsp
  401b38:	48 83 c4 08          	add    $0x8,%rsp
  401b3c:	c3                   	retq   
