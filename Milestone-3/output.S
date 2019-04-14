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
	#=,var1,5,
	movl $5, -8(%ebp)
	#=,var4,1,
	movl $1, -28(%ebp)
	#=,var6,1,
	movl $1, -40(%ebp)
	#=,var2,var6,
	movl -40(%ebp), %eax
	movl %eax, -16(%ebp)
	#label,label2,

label2:

	#<,var7,var2,var1,
	movl -16(%ebp), %eax
	movl -8(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -140(%ebp)
	#=,var9,var7,
	movl -140(%ebp), %eax
	movl %eax, -148(%ebp)
	#=,var10,1,
	movl $1, -152(%ebp)
	#-,var9,var10,var9,
	movl -152(%ebp), %eax
	movl -148(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -148(%ebp)
	#ifgoto,var9,label3,
	movl -148(%ebp), %eax
	cmp $0, %eax
	je label3
	#+,var8,var2,var6,
	movl -16(%ebp), %eax
	movl -40(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -144(%ebp)
	#=,var2,var8,
	movl -144(%ebp), %eax
	movl %eax, -16(%ebp)
	#*,var11,var4,var2,
	movl -28(%ebp), %eax
	movl -16(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -156(%ebp)
	#=,var4,var11,
	movl -156(%ebp), %eax
	movl %eax, -28(%ebp)
	#goto,label2,
	jmp label2
	#label,label3,

label3:

	#print,var4,
	pushl %eax
	pushl %ecx
	pushl %edx
	pushl -28(%ebp)
	pushl $outFormatInt
	call printf
	addl $8, %esp
	popl %edx
	popl %ecx
	popl %eax
	#retvoid,

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
