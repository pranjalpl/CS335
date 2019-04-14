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
	
#=,var1,1,
	movl $1, -8(%ebp)
	
#=,var3,1,
	movl $1, -20(%ebp)
	
#=,var5,1,
	movl $1, -32(%ebp)
	
#=,var7,25,
	movl $25, -44(%ebp)
	
#=,var9,14,
	movl $14, -56(%ebp)
	
#=,var11,12,
	movl $12, -68(%ebp)
	
#=,var13,1,
	movl $1, -80(%ebp)
	
#=,var15,1,
	movl $1, -92(%ebp)
	
#=,var17,1,
	movl $1, -104(%ebp)
	
#=,var19,0,
	movl $0, -116(%ebp)
	
#=,var21,0,
	movl $0, -128(%ebp)
	
#=,var13,var17,
	movl -104(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label2,

label2:

	
#<=,var22,var13,var7,
	movl -80(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -228(%ebp)
	
#=,var24,var22,
	movl -228(%ebp), %eax
	movl %eax, -236(%ebp)
	
#=,var25,1,
	movl $1, -240(%ebp)
	
#-,var24,var25,var24,
	movl -240(%ebp), %eax
	movl -236(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -236(%ebp)
	
#ifgoto,var24,label3,
	movl -236(%ebp), %eax
	cmp $0, %eax
	je label3
	
#=,var15,var17,
	movl -104(%ebp), %eax
	movl %eax, -92(%ebp)
	
#label,label4,

label4:

	
#<=,var26,var15,var7,
	movl -92(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -112(%ebp)
	
#=,var28,var26,
	movl -112(%ebp), %eax
	movl %eax, -120(%ebp)
	
#=,var29,1,
	movl $1, -124(%ebp)
	
#-,var28,var29,var28,
	movl -124(%ebp), %eax
	movl -120(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -120(%ebp)
	
#ifgoto,var28,label5,
	movl -120(%ebp), %eax
	cmp $0, %eax
	je label5
	
#=,var30,10,
	movl $10, -128(%ebp)
	
#+,var31,var19,var30,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -132(%ebp)
	
#=,var19,var31,
	movl -132(%ebp), %eax
	movl %eax, -116(%ebp)
	
#+,var27,var15,var17,
	movl -92(%ebp), %eax
	movl -104(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -116(%ebp)
	
#=,var15,var27,
	movl -116(%ebp), %eax
	movl %eax, -92(%ebp)
	
#goto,label4,
	jmp label4
	
#label,label5,

label5:

	
#+,var23,var13,var17,
	movl -80(%ebp), %eax
	movl -104(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -232(%ebp)
	
#=,var13,var23,
	movl -232(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label2,
	jmp label2
	
#label,label3,

label3:

	
#print,var11,
	pushl %eax
	pushl %ecx
	pushl %edx
	pushl -68(%ebp)
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
