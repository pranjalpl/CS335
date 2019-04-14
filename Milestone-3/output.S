.data

outFormatInt:
	.asciz	"%d\n"
outFormatStr:
	.asciz	"%s\n"
inFormat:
	.ascii	"%d"

.text

.global main

main:

	call mainDriver
	jmp exit


mainDriver:

	pushl %ebp
	movl %esp, %ebp
	#goto,label0,
	#label0:,
	#retvoid,

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
