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
	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $24, %esp
	
#=,var1,3,
	movl $3, -8(%ebp)
	
#=,var2,42,
	movl $42, -12(%ebp)
	
#=,var4,0,
	movl $0, -20(%ebp)
	
#-,var3,var4,var2,
	movl -20(%ebp), %eax
	movl -12(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -16(%ebp)
	
#=,var1,var3,
	movl -16(%ebp), %eax
	movl %eax, -8(%ebp)
	
#print,var1,
	push -8(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
