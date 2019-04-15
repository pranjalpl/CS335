.data

var0:
	.int	0
var1:
	.int	0
var2:
	.int	0
var4:
	.int	0
var5:
	.int	0
var6:
	.int	0
var3:
	.int	0
var7:
	.int	0
var8:
	.int	0
var9:
	.int	0
var10:
	.int	0
var11:
	.int	0
var12:
	.int	0
var13:
	.int	0
var14:
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
	# 1, goto, label0
	jmp label0
	# 2, label, label1

label1:

	pushl %ebp
	movl %esp,  %ebp
	# 3, pload, var0, 0
	movl 0x8(%ebp), %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	movl $eax, %eax
	# 4, =, var1, 1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	movl $1, var1
	# 5, ==, var2, var0, var1
	movl %eax, var0
	cmp (var1), %eax
	sete %al
	movzbl %al, %eax
	# 6, =, var4, var2
	movl %eax, %ebx
	# 7, =, var5, 0
	movl $0, var5
	movl $0, var5
	movl $0, var5
	movl $0, var5
	movl $0, var5
	movl $0, var5
	movl $0, var5
	movl $0, var5
	# 8, !=, var4, var4, var5
	movl %ebx, var4
	cmp (var5), %ebx
	movl %eax, var2
	setne %al
	movzbl %al, %ebx
	movl (var2), %eax
	# 9, =, var6, 1
	movl $1, var6
	movl $1, var6
	movl $1, var6
	movl $1, var6
	movl $1, var6
	movl $1, var6
	movl $1, var6
	movl $1, var6
	# 10, -, var4, var4, var6
	movl %ebx, var4
	subl (var6), %ebx
	movl %eax, var2
	movl %ebx, var4
	# 11, ifgoto, var4, label2
	cmp $0, (var4)
	jne label2
	# 12, =, var3, 1
	movl $1, var3
	movl $1, var3
	movl $1, var3
	movl $1, var3
	movl $1, var3
	movl $1, var3
	movl $1, var3
	movl $1, var3
	# 13, retint, var3
	movl (var3), %eax
	leave
	ret
	# 14, goto, label3
	jmp label3
	# 15, label, label2

label2:

	# 16, label, label3

label3:

	# 17, =, var7, 1
	movl $1, var7
	movl $1, var7
	movl $1, var7
	movl $1, var7
	movl $1, var7
	movl $1, var7
	movl $1, var7
	movl $1, var7
	# 18, -, var8, var0, var7
	movl (var0), %eax
	subl (var7), %eax
	# 19, push, var0
	pushl var0
	# 20, push, var8
	pushl %eax
	movl %eax, var8
	# 21, callint, var9, label1
	call label1
	movl %eax, var9
	# 22, pop, var10
	popl var10
	# 23, pop, var0
	popl var0
	# 24, x, var11, var0, var9
	movl (var0), %eax
	imul (var9), %eax
	movl %eax, var11
	# 25, retint, var11
	movl (var11), %eax
	leave
	ret
	# 26, label, label0

label0:

	# 27, scan, var12
	pushl $var12
	pushl $inFormat
	call scanf
	# 28, push, var12
	pushl var12
	# 29, push, var12
	pushl var12
	# 30, callint, var13, label1
	call label1
	movl %eax, var13
	# 31, pop, var14
	popl var14
	# 32, pop, var12
	popl var12
	# 33, printint, var13
	pushl var13
	pushl $outFormatInt
	call printf

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
