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
	movl $1, -8(%ebp)
	movl $1, -20(%ebp)
	movl -8(%ebp), %eax
	movl -20(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %ecx, %eax
	movl %ecx, -32(%ebp)
	movl -32(%ebp), %eax
	movl %eax, -28(%ebp)
	movl -32(%ebp), %eax
	movl -8(%ebp), %ebx
	cmp %eax, %ebx
	sete %al
	movzbl %al, %eax
	movl %ecx, -36(%ebp)
	movl -36(%ebp), %eax
	movl %eax, -40(%ebp)
	movl $1, -44(%ebp)
	movl -44(%ebp), %eax
	movl -40(%ebp), %ebx
	subl %%eax, %%ebx
	movl %ebx, -40(%ebp)
