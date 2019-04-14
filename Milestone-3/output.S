.data

outFormatInt:
	.string	"%d\n"
outFormatStr:
	.string	"%s\n"
inFormat:
	.string	"%d"

.text

.global main

main:

	call mainDriver
	jmp exit


mainDriver:

	
#goto,label0,
	jmp label0
	
#label1:,

label1:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $44, %esp
	
#pop-param,0,var3,
	movl 8(%ebp), %eax
	movl %eax, -28(%ebp)
	
#pop-param,1,var2,
	movl 12(%ebp), %eax
	movl %eax, -20(%ebp)
	
#pop-param,2,var1,
	movl 16(%ebp), %eax
	movl %eax, -12(%ebp)
	
#pop-param,3,var0,
	movl 20(%ebp), %eax
	movl %eax, -4(%ebp)
	
#-,var4,var2,var3,
	movl -20(%ebp), %eax
	movl -28(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -32(%ebp)
	
#+,var5,var1,var4,
	movl -12(%ebp), %eax
	movl -32(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -36(%ebp)
	
#+,var6,var0,var5,
	movl -4(%ebp), %eax
	movl -36(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -40(%ebp)
	
#retint,var6,
	movl -40(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $28, %esp
	
#save_registers,
	
#=,var8,1,
	movl $1, -8(%ebp)
	
#=,var9,5,
	movl $5, -12(%ebp)
	
#=,var10,3,
	movl $3, -16(%ebp)
	
#=,var11,4,
	movl $4, -20(%ebp)
	
#callint,var12,label1,var8,var9,var10,var11,
	pushl -20(%ebp)
	pushl -16(%ebp)
	pushl -12(%ebp)
	pushl -8(%ebp)
	call label1
	addl $16, %esp
	movl %eax, -24(%ebp)
	
#restore_registers,
	
#=,var7,var12,
	movl -24(%ebp), %eax
	movl %eax, -4(%ebp)
	
#print,var12,
	push -24(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
