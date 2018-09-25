
badchars32:     file format elf32-i386


Disassembly of section .init:

08048440 <_init>:
 8048440:	53                   	push   %ebx
 8048441:	83 ec 08             	sub    $0x8,%esp
 8048444:	e8 27 01 00 00       	call   8048570 <__x86.get_pc_thunk.bx>
 8048449:	81 c3 b7 1b 00 00    	add    $0x1bb7,%ebx
 804844f:	8b 83 fc ff ff ff    	mov    -0x4(%ebx),%eax
 8048455:	85 c0                	test   %eax,%eax
 8048457:	74 05                	je     804845e <_init+0x1e>
 8048459:	e8 d2 00 00 00       	call   8048530 <memset@plt+0x10>
 804845e:	83 c4 08             	add    $0x8,%esp
 8048461:	5b                   	pop    %ebx
 8048462:	c3                   	ret    

Disassembly of section .plt:

08048470 <printf@plt-0x10>:
 8048470:	ff 35 04 a0 04 08    	pushl  0x804a004
 8048476:	ff 25 08 a0 04 08    	jmp    *0x804a008
 804847c:	00 00                	add    %al,(%eax)
	...

08048480 <printf@plt>:
 8048480:	ff 25 0c a0 04 08    	jmp    *0x804a00c
 8048486:	68 00 00 00 00       	push   $0x0
 804848b:	e9 e0 ff ff ff       	jmp    8048470 <_init+0x30>

08048490 <free@plt>:
 8048490:	ff 25 10 a0 04 08    	jmp    *0x804a010
 8048496:	68 08 00 00 00       	push   $0x8
 804849b:	e9 d0 ff ff ff       	jmp    8048470 <_init+0x30>

080484a0 <memcpy@plt>:
 80484a0:	ff 25 14 a0 04 08    	jmp    *0x804a014
 80484a6:	68 10 00 00 00       	push   $0x10
 80484ab:	e9 c0 ff ff ff       	jmp    8048470 <_init+0x30>

080484b0 <fgets@plt>:
 80484b0:	ff 25 18 a0 04 08    	jmp    *0x804a018
 80484b6:	68 18 00 00 00       	push   $0x18
 80484bb:	e9 b0 ff ff ff       	jmp    8048470 <_init+0x30>

080484c0 <malloc@plt>:
 80484c0:	ff 25 1c a0 04 08    	jmp    *0x804a01c
 80484c6:	68 20 00 00 00       	push   $0x20
 80484cb:	e9 a0 ff ff ff       	jmp    8048470 <_init+0x30>

080484d0 <puts@plt>:
 80484d0:	ff 25 20 a0 04 08    	jmp    *0x804a020
 80484d6:	68 28 00 00 00       	push   $0x28
 80484db:	e9 90 ff ff ff       	jmp    8048470 <_init+0x30>

080484e0 <system@plt>:
 80484e0:	ff 25 24 a0 04 08    	jmp    *0x804a024
 80484e6:	68 30 00 00 00       	push   $0x30
 80484eb:	e9 80 ff ff ff       	jmp    8048470 <_init+0x30>

080484f0 <exit@plt>:
 80484f0:	ff 25 28 a0 04 08    	jmp    *0x804a028
 80484f6:	68 38 00 00 00       	push   $0x38
 80484fb:	e9 70 ff ff ff       	jmp    8048470 <_init+0x30>

08048500 <__libc_start_main@plt>:
 8048500:	ff 25 2c a0 04 08    	jmp    *0x804a02c
 8048506:	68 40 00 00 00       	push   $0x40
 804850b:	e9 60 ff ff ff       	jmp    8048470 <_init+0x30>

08048510 <setvbuf@plt>:
 8048510:	ff 25 30 a0 04 08    	jmp    *0x804a030
 8048516:	68 48 00 00 00       	push   $0x48
 804851b:	e9 50 ff ff ff       	jmp    8048470 <_init+0x30>

08048520 <memset@plt>:
 8048520:	ff 25 34 a0 04 08    	jmp    *0x804a034
 8048526:	68 50 00 00 00       	push   $0x50
 804852b:	e9 40 ff ff ff       	jmp    8048470 <_init+0x30>

Disassembly of section .plt.got:

08048530 <.plt.got>:
 8048530:	ff 25 fc 9f 04 08    	jmp    *0x8049ffc
 8048536:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

08048540 <_start>:
 8048540:	31 ed                	xor    %ebp,%ebp
 8048542:	5e                   	pop    %esi
 8048543:	89 e1                	mov    %esp,%ecx
 8048545:	83 e4 f0             	and    $0xfffffff0,%esp
 8048548:	50                   	push   %eax
 8048549:	54                   	push   %esp
 804854a:	52                   	push   %edx
 804854b:	68 00 89 04 08       	push   $0x8048900
 8048550:	68 a0 88 04 08       	push   $0x80488a0
 8048555:	51                   	push   %ecx
 8048556:	56                   	push   %esi
 8048557:	68 3b 86 04 08       	push   $0x804863b
 804855c:	e8 9f ff ff ff       	call   8048500 <__libc_start_main@plt>
 8048561:	f4                   	hlt    
 8048562:	66 90                	xchg   %ax,%ax
 8048564:	66 90                	xchg   %ax,%ax
 8048566:	66 90                	xchg   %ax,%ax
 8048568:	66 90                	xchg   %ax,%ax
 804856a:	66 90                	xchg   %ax,%ax
 804856c:	66 90                	xchg   %ax,%ax
 804856e:	66 90                	xchg   %ax,%ax

08048570 <__x86.get_pc_thunk.bx>:
 8048570:	8b 1c 24             	mov    (%esp),%ebx
 8048573:	c3                   	ret    
 8048574:	66 90                	xchg   %ax,%ax
 8048576:	66 90                	xchg   %ax,%ax
 8048578:	66 90                	xchg   %ax,%ax
 804857a:	66 90                	xchg   %ax,%ax
 804857c:	66 90                	xchg   %ax,%ax
 804857e:	66 90                	xchg   %ax,%ax

08048580 <deregister_tm_clones>:
 8048580:	b8 43 a0 04 08       	mov    $0x804a043,%eax
 8048585:	2d 40 a0 04 08       	sub    $0x804a040,%eax
 804858a:	83 f8 06             	cmp    $0x6,%eax
 804858d:	76 1a                	jbe    80485a9 <deregister_tm_clones+0x29>
 804858f:	b8 00 00 00 00       	mov    $0x0,%eax
 8048594:	85 c0                	test   %eax,%eax
 8048596:	74 11                	je     80485a9 <deregister_tm_clones+0x29>
 8048598:	55                   	push   %ebp
 8048599:	89 e5                	mov    %esp,%ebp
 804859b:	83 ec 14             	sub    $0x14,%esp
 804859e:	68 40 a0 04 08       	push   $0x804a040
 80485a3:	ff d0                	call   *%eax
 80485a5:	83 c4 10             	add    $0x10,%esp
 80485a8:	c9                   	leave  
 80485a9:	f3 c3                	repz ret 
 80485ab:	90                   	nop
 80485ac:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi

080485b0 <register_tm_clones>:
 80485b0:	b8 40 a0 04 08       	mov    $0x804a040,%eax
 80485b5:	2d 40 a0 04 08       	sub    $0x804a040,%eax
 80485ba:	c1 f8 02             	sar    $0x2,%eax
 80485bd:	89 c2                	mov    %eax,%edx
 80485bf:	c1 ea 1f             	shr    $0x1f,%edx
 80485c2:	01 d0                	add    %edx,%eax
 80485c4:	d1 f8                	sar    %eax
 80485c6:	74 1b                	je     80485e3 <register_tm_clones+0x33>
 80485c8:	ba 00 00 00 00       	mov    $0x0,%edx
 80485cd:	85 d2                	test   %edx,%edx
 80485cf:	74 12                	je     80485e3 <register_tm_clones+0x33>
 80485d1:	55                   	push   %ebp
 80485d2:	89 e5                	mov    %esp,%ebp
 80485d4:	83 ec 10             	sub    $0x10,%esp
 80485d7:	50                   	push   %eax
 80485d8:	68 40 a0 04 08       	push   $0x804a040
 80485dd:	ff d2                	call   *%edx
 80485df:	83 c4 10             	add    $0x10,%esp
 80485e2:	c9                   	leave  
 80485e3:	f3 c3                	repz ret 
 80485e5:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 80485e9:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi

080485f0 <__do_global_dtors_aux>:
 80485f0:	80 3d 68 a0 04 08 00 	cmpb   $0x0,0x804a068
 80485f7:	75 13                	jne    804860c <__do_global_dtors_aux+0x1c>
 80485f9:	55                   	push   %ebp
 80485fa:	89 e5                	mov    %esp,%ebp
 80485fc:	83 ec 08             	sub    $0x8,%esp
 80485ff:	e8 7c ff ff ff       	call   8048580 <deregister_tm_clones>
 8048604:	c6 05 68 a0 04 08 01 	movb   $0x1,0x804a068
 804860b:	c9                   	leave  
 804860c:	f3 c3                	repz ret 
 804860e:	66 90                	xchg   %ax,%ax

08048610 <frame_dummy>:
 8048610:	b8 10 9f 04 08       	mov    $0x8049f10,%eax
 8048615:	8b 10                	mov    (%eax),%edx
 8048617:	85 d2                	test   %edx,%edx
 8048619:	75 05                	jne    8048620 <frame_dummy+0x10>
 804861b:	eb 93                	jmp    80485b0 <register_tm_clones>
 804861d:	8d 76 00             	lea    0x0(%esi),%esi
 8048620:	ba 00 00 00 00       	mov    $0x0,%edx
 8048625:	85 d2                	test   %edx,%edx
 8048627:	74 f2                	je     804861b <frame_dummy+0xb>
 8048629:	55                   	push   %ebp
 804862a:	89 e5                	mov    %esp,%ebp
 804862c:	83 ec 14             	sub    $0x14,%esp
 804862f:	50                   	push   %eax
 8048630:	ff d2                	call   *%edx
 8048632:	83 c4 10             	add    $0x10,%esp
 8048635:	c9                   	leave  
 8048636:	e9 75 ff ff ff       	jmp    80485b0 <register_tm_clones>

0804863b <main>:
 804863b:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 804863f:	83 e4 f0             	and    $0xfffffff0,%esp
 8048642:	ff 71 fc             	pushl  -0x4(%ecx)
 8048645:	55                   	push   %ebp
 8048646:	89 e5                	mov    %esp,%ebp
 8048648:	51                   	push   %ecx
 8048649:	83 ec 04             	sub    $0x4,%esp
 804864c:	a1 64 a0 04 08       	mov    0x804a064,%eax
 8048651:	6a 00                	push   $0x0
 8048653:	6a 02                	push   $0x2
 8048655:	6a 00                	push   $0x0
 8048657:	50                   	push   %eax
 8048658:	e8 b3 fe ff ff       	call   8048510 <setvbuf@plt>
 804865d:	83 c4 10             	add    $0x10,%esp
 8048660:	a1 40 a0 04 08       	mov    0x804a040,%eax
 8048665:	6a 00                	push   $0x0
 8048667:	6a 02                	push   $0x2
 8048669:	6a 00                	push   $0x0
 804866b:	50                   	push   %eax
 804866c:	e8 9f fe ff ff       	call   8048510 <setvbuf@plt>
 8048671:	83 c4 10             	add    $0x10,%esp
 8048674:	83 ec 0c             	sub    $0xc,%esp
 8048677:	68 20 89 04 08       	push   $0x8048920
 804867c:	e8 4f fe ff ff       	call   80484d0 <puts@plt>
 8048681:	83 c4 10             	add    $0x10,%esp
 8048684:	83 ec 0c             	sub    $0xc,%esp
 8048687:	68 39 89 04 08       	push   $0x8048939
 804868c:	e8 3f fe ff ff       	call   80484d0 <puts@plt>
 8048691:	83 c4 10             	add    $0x10,%esp
 8048694:	e8 1d 00 00 00       	call   80486b6 <pwnme>
 8048699:	83 ec 0c             	sub    $0xc,%esp
 804869c:	68 41 89 04 08       	push   $0x8048941
 80486a1:	e8 2a fe ff ff       	call   80484d0 <puts@plt>
 80486a6:	83 c4 10             	add    $0x10,%esp
 80486a9:	b8 00 00 00 00       	mov    $0x0,%eax
 80486ae:	8b 4d fc             	mov    -0x4(%ebp),%ecx
 80486b1:	c9                   	leave  
 80486b2:	8d 61 fc             	lea    -0x4(%ecx),%esp
 80486b5:	c3                   	ret    

080486b6 <pwnme>:
 80486b6:	55                   	push   %ebp
 80486b7:	89 e5                	mov    %esp,%ebp
 80486b9:	83 ec 38             	sub    $0x38,%esp
 80486bc:	c7 45 d0 00 00 00 00 	movl   $0x0,-0x30(%ebp)
 80486c3:	83 ec 0c             	sub    $0xc,%esp
 80486c6:	68 00 02 00 00       	push   $0x200
 80486cb:	e8 f0 fd ff ff       	call   80484c0 <malloc@plt>
 80486d0:	83 c4 10             	add    $0x10,%esp
 80486d3:	89 45 d4             	mov    %eax,-0x2c(%ebp)
 80486d6:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 80486d9:	85 c0                	test   %eax,%eax
 80486db:	74 18                	je     80486f5 <pwnme+0x3f>
 80486dd:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 80486e0:	83 ec 04             	sub    $0x4,%esp
 80486e3:	68 00 02 00 00       	push   $0x200
 80486e8:	6a 00                	push   $0x0
 80486ea:	50                   	push   %eax
 80486eb:	e8 30 fe ff ff       	call   8048520 <memset@plt>
 80486f0:	83 c4 10             	add    $0x10,%esp
 80486f3:	eb 0a                	jmp    80486ff <pwnme+0x49>
 80486f5:	83 ec 0c             	sub    $0xc,%esp
 80486f8:	6a 01                	push   $0x1
 80486fa:	e8 f1 fd ff ff       	call   80484f0 <exit@plt>
 80486ff:	83 ec 04             	sub    $0x4,%esp
 8048702:	6a 20                	push   $0x20
 8048704:	6a 00                	push   $0x0
 8048706:	8d 45 d0             	lea    -0x30(%ebp),%eax
 8048709:	83 c0 08             	add    $0x8,%eax
 804870c:	50                   	push   %eax
 804870d:	e8 0e fe ff ff       	call   8048520 <memset@plt>
 8048712:	83 c4 10             	add    $0x10,%esp
 8048715:	83 ec 0c             	sub    $0xc,%esp
 8048718:	68 4c 89 04 08       	push   $0x804894c
 804871d:	e8 ae fd ff ff       	call   80484d0 <puts@plt>
 8048722:	83 c4 10             	add    $0x10,%esp
 8048725:	83 ec 0c             	sub    $0xc,%esp
 8048728:	68 70 89 04 08       	push   $0x8048970
 804872d:	e8 4e fd ff ff       	call   8048480 <printf@plt>
 8048732:	83 c4 10             	add    $0x10,%esp
 8048735:	8b 15 60 a0 04 08    	mov    0x804a060,%edx
 804873b:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 804873e:	83 ec 04             	sub    $0x4,%esp
 8048741:	52                   	push   %edx
 8048742:	68 00 02 00 00       	push   $0x200
 8048747:	50                   	push   %eax
 8048748:	e8 63 fd ff ff       	call   80484b0 <fgets@plt>
 804874d:	83 c4 10             	add    $0x10,%esp
 8048750:	89 45 d4             	mov    %eax,-0x2c(%ebp)
 8048753:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048756:	83 ec 08             	sub    $0x8,%esp
 8048759:	68 00 02 00 00       	push   $0x200
 804875e:	50                   	push   %eax
 804875f:	e8 5e 00 00 00       	call   80487c2 <nstrlen>
 8048764:	83 c4 10             	add    $0x10,%esp
 8048767:	89 45 d0             	mov    %eax,-0x30(%ebp)
 804876a:	8b 55 d0             	mov    -0x30(%ebp),%edx
 804876d:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048770:	83 ec 08             	sub    $0x8,%esp
 8048773:	52                   	push   %edx
 8048774:	50                   	push   %eax
 8048775:	e8 87 00 00 00       	call   8048801 <checkBadchars>
 804877a:	83 c4 10             	add    $0x10,%esp
 804877d:	8b 55 d0             	mov    -0x30(%ebp),%edx
 8048780:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048783:	83 ec 04             	sub    $0x4,%esp
 8048786:	52                   	push   %edx
 8048787:	50                   	push   %eax
 8048788:	8d 45 d0             	lea    -0x30(%ebp),%eax
 804878b:	83 c0 08             	add    $0x8,%eax
 804878e:	50                   	push   %eax
 804878f:	e8 0c fd ff ff       	call   80484a0 <memcpy@plt>
 8048794:	83 c4 10             	add    $0x10,%esp
 8048797:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 804879a:	83 ec 0c             	sub    $0xc,%esp
 804879d:	50                   	push   %eax
 804879e:	e8 ed fc ff ff       	call   8048490 <free@plt>
 80487a3:	83 c4 10             	add    $0x10,%esp
 80487a6:	90                   	nop
 80487a7:	c9                   	leave  
 80487a8:	c3                   	ret    

080487a9 <usefulFunction>:
 80487a9:	55                   	push   %ebp
 80487aa:	89 e5                	mov    %esp,%ebp
 80487ac:	83 ec 08             	sub    $0x8,%esp
 80487af:	83 ec 0c             	sub    $0xc,%esp
 80487b2:	68 73 89 04 08       	push   $0x8048973
 80487b7:	e8 24 fd ff ff       	call   80484e0 <system@plt>
 80487bc:	83 c4 10             	add    $0x10,%esp
 80487bf:	90                   	nop
 80487c0:	c9                   	leave  
 80487c1:	c3                   	ret    

080487c2 <nstrlen>:
 80487c2:	55                   	push   %ebp
 80487c3:	89 e5                	mov    %esp,%ebp
 80487c5:	83 ec 10             	sub    $0x10,%esp
 80487c8:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 80487cf:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 80487d6:	eb 1c                	jmp    80487f4 <nstrlen+0x32>
 80487d8:	8b 55 08             	mov    0x8(%ebp),%edx
 80487db:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80487de:	01 d0                	add    %edx,%eax
 80487e0:	0f b6 00             	movzbl (%eax),%eax
 80487e3:	3c 0a                	cmp    $0xa,%al
 80487e5:	75 09                	jne    80487f0 <nstrlen+0x2e>
 80487e7:	83 45 fc 01          	addl   $0x1,-0x4(%ebp)
 80487eb:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80487ee:	eb 0f                	jmp    80487ff <nstrlen+0x3d>
 80487f0:	83 45 fc 01          	addl   $0x1,-0x4(%ebp)
 80487f4:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80487f7:	3b 45 0c             	cmp    0xc(%ebp),%eax
 80487fa:	72 dc                	jb     80487d8 <nstrlen+0x16>
 80487fc:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80487ff:	c9                   	leave  
 8048800:	c3                   	ret    

08048801 <checkBadchars>:
 8048801:	55                   	push   %ebp
 8048802:	89 e5                	mov    %esp,%ebp
 8048804:	83 ec 10             	sub    $0x10,%esp
 8048807:	c6 45 f0 62          	movb   $0x62,-0x10(%ebp)
 804880b:	c6 45 f1 69          	movb   $0x69,-0xf(%ebp)
 804880f:	c6 45 f2 63          	movb   $0x63,-0xe(%ebp)
 8048813:	c6 45 f3 2f          	movb   $0x2f,-0xd(%ebp)
 8048817:	c6 45 f4 20          	movb   $0x20,-0xc(%ebp)
 804881b:	c6 45 f5 66          	movb   $0x66,-0xb(%ebp)
 804881f:	c6 45 f6 6e          	movb   $0x6e,-0xa(%ebp)
 8048823:	c6 45 f7 73          	movb   $0x73,-0x9(%ebp)
 8048827:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 804882e:	c7 45 f8 00 00 00 00 	movl   $0x0,-0x8(%ebp)
 8048835:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 804883c:	eb 3e                	jmp    804887c <checkBadchars+0x7b>
 804883e:	c7 45 f8 00 00 00 00 	movl   $0x0,-0x8(%ebp)
 8048845:	eb 2b                	jmp    8048872 <checkBadchars+0x71>
 8048847:	8b 55 08             	mov    0x8(%ebp),%edx
 804884a:	8b 45 fc             	mov    -0x4(%ebp),%eax
 804884d:	01 d0                	add    %edx,%eax
 804884f:	0f b6 10             	movzbl (%eax),%edx
 8048852:	8d 4d f0             	lea    -0x10(%ebp),%ecx
 8048855:	8b 45 f8             	mov    -0x8(%ebp),%eax
 8048858:	01 c8                	add    %ecx,%eax
 804885a:	0f b6 00             	movzbl (%eax),%eax
 804885d:	38 c2                	cmp    %al,%dl
 804885f:	75 0d                	jne    804886e <checkBadchars+0x6d>
 8048861:	8b 55 08             	mov    0x8(%ebp),%edx
 8048864:	8b 45 fc             	mov    -0x4(%ebp),%eax
 8048867:	01 d0                	add    %edx,%eax
 8048869:	c6 00 eb             	movb   $0xeb,(%eax)
 804886c:	eb 0a                	jmp    8048878 <checkBadchars+0x77>
 804886e:	83 45 f8 01          	addl   $0x1,-0x8(%ebp)
 8048872:	83 7d f8 07          	cmpl   $0x7,-0x8(%ebp)
 8048876:	76 cf                	jbe    8048847 <checkBadchars+0x46>
 8048878:	83 45 fc 01          	addl   $0x1,-0x4(%ebp)
 804887c:	8b 45 fc             	mov    -0x4(%ebp),%eax
 804887f:	3b 45 0c             	cmp    0xc(%ebp),%eax
 8048882:	72 ba                	jb     804883e <checkBadchars+0x3d>
 8048884:	90                   	nop
 8048885:	c9                   	leave  
 8048886:	c3                   	ret    
 8048887:	66 90                	xchg   %ax,%ax
 8048889:	66 90                	xchg   %ax,%ax
 804888b:	66 90                	xchg   %ax,%ax
 804888d:	66 90                	xchg   %ax,%ax
 804888f:	90                   	nop

08048890 <usefulGadgets>:
 8048890:	30 0b                	xor    %cl,(%ebx)
 8048892:	c3                   	ret    
 8048893:	89 37                	mov    %esi,(%edi)
 8048895:	c3                   	ret    
 8048896:	5b                   	pop    %ebx
 8048897:	59                   	pop    %ecx
 8048898:	c3                   	ret    
 8048899:	5e                   	pop    %esi
 804889a:	5f                   	pop    %edi
 804889b:	c3                   	ret    
 804889c:	66 90                	xchg   %ax,%ax
 804889e:	66 90                	xchg   %ax,%ax

080488a0 <__libc_csu_init>:
 80488a0:	55                   	push   %ebp
 80488a1:	57                   	push   %edi
 80488a2:	56                   	push   %esi
 80488a3:	53                   	push   %ebx
 80488a4:	e8 c7 fc ff ff       	call   8048570 <__x86.get_pc_thunk.bx>
 80488a9:	81 c3 57 17 00 00    	add    $0x1757,%ebx
 80488af:	83 ec 0c             	sub    $0xc,%esp
 80488b2:	8b 6c 24 20          	mov    0x20(%esp),%ebp
 80488b6:	8d b3 0c ff ff ff    	lea    -0xf4(%ebx),%esi
 80488bc:	e8 7f fb ff ff       	call   8048440 <_init>
 80488c1:	8d 83 08 ff ff ff    	lea    -0xf8(%ebx),%eax
 80488c7:	29 c6                	sub    %eax,%esi
 80488c9:	c1 fe 02             	sar    $0x2,%esi
 80488cc:	85 f6                	test   %esi,%esi
 80488ce:	74 25                	je     80488f5 <__libc_csu_init+0x55>
 80488d0:	31 ff                	xor    %edi,%edi
 80488d2:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi
 80488d8:	83 ec 04             	sub    $0x4,%esp
 80488db:	ff 74 24 2c          	pushl  0x2c(%esp)
 80488df:	ff 74 24 2c          	pushl  0x2c(%esp)
 80488e3:	55                   	push   %ebp
 80488e4:	ff 94 bb 08 ff ff ff 	call   *-0xf8(%ebx,%edi,4)
 80488eb:	83 c7 01             	add    $0x1,%edi
 80488ee:	83 c4 10             	add    $0x10,%esp
 80488f1:	39 f7                	cmp    %esi,%edi
 80488f3:	75 e3                	jne    80488d8 <__libc_csu_init+0x38>
 80488f5:	83 c4 0c             	add    $0xc,%esp
 80488f8:	5b                   	pop    %ebx
 80488f9:	5e                   	pop    %esi
 80488fa:	5f                   	pop    %edi
 80488fb:	5d                   	pop    %ebp
 80488fc:	c3                   	ret    
 80488fd:	8d 76 00             	lea    0x0(%esi),%esi

08048900 <__libc_csu_fini>:
 8048900:	f3 c3                	repz ret 

Disassembly of section .fini:

08048904 <_fini>:
 8048904:	53                   	push   %ebx
 8048905:	83 ec 08             	sub    $0x8,%esp
 8048908:	e8 63 fc ff ff       	call   8048570 <__x86.get_pc_thunk.bx>
 804890d:	81 c3 f3 16 00 00    	add    $0x16f3,%ebx
 8048913:	83 c4 08             	add    $0x8,%esp
 8048916:	5b                   	pop    %ebx
 8048917:	c3                   	ret    
