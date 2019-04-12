.data

var1:
	.int	0
var2:
	.int	0
var3:
	.int	0
outFormatInt:
	.asciz	"%d\n"
outFormatStr:
	.asciz	"%s\n"
inFormat:
	.ascii	"%d"

.text

.global main

main:

	call mainMandal
	jmp exit


mainMandal:

	pushl %ebp
	movl %esp, %ebp
	# 1, =, var1, 3
	movl $3, var1
	movl $3, var1
	movl $3, var1
	movl $3, var1
	movl $3, var1
	movl $3, var1
	movl $3, var1
	movl $3, var1
	# 2, goto, label0
	jmp label0
	# 3, label, label1

label1:

	pushl %ebp
	movl %esp,  %ebp
	# 4, retint, var1
	movl (var1), %eax
	leave
	ret
	# 5, label, label0

label0:

	# 6, push, var2
	pushl var2
	# 7, callint, var3, label1
	call label1
	movl %eax, var3
	# 8, pop, var2
	popl var2
	# 9, =, var2, var3
	movl (var3), %eax
	# 10, printint, var3
	pushl var3
	pushl $outFormatInt
	call printf
	# 11, retvoid
	leave
	ret

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
