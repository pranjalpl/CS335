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
	sub $112, %esp
	
#pop-param,1,var0,
	movl 12(%ebp), %eax
	movl %eax, -4(%ebp)
	
#pop-param,0,var1,
	movl 8(%ebp), %eax
	movl %eax, -12(%ebp)
	
#=,var2,0,
	movl $0, -16(%ebp)
	
#==,var3,var1,var2,
	movl -12(%ebp), %eax
	movl -16(%ebp), %ebx
	cmp %eax, %ebx
	setne %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -20(%ebp)
	
#ifgoto,var3,label2,
	movl -20(%ebp), %eax
	cmp $0, %eax
	je label2
	
#=,var4,1,
	movl $1, -64(%ebp)
	
#+,var5,var0,var4,
	movl -4(%ebp), %eax
	movl -64(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -68(%ebp)
	
#retint,var5,
	movl -68(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#goto,label3,
	jmp label3
	
#label,label2,

label2:

	
#label,label3,

label3:

	
#=,var6,0,
	movl $0, -24(%ebp)
	
#>,var7,var1,var6,
	movl -12(%ebp), %eax
	movl -24(%ebp), %ebx
	cmp %eax, %ebx
	setge %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -28(%ebp)
	
#=,var8,0,
	movl $0, -32(%ebp)
	
#==,var9,var0,var8,
	movl -4(%ebp), %eax
	movl -32(%ebp), %ebx
	cmp %eax, %ebx
	setne %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -36(%ebp)
	
#&&,var10,var7,var9,
	movl -28(%ebp), %eax
	movl -36(%ebp), %ebx
	and %eax, %ebx
	movl %ebx, -40(%ebp)
	
#ifgoto,var10,label4,
	movl -40(%ebp), %eax
	cmp $0, %eax
	je label4
	
#save_registers,
	
#=,var11,1,
	movl $1, -72(%ebp)
	
#-,var12,var1,var11,
	movl -12(%ebp), %eax
	movl -72(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -76(%ebp)
	
#=,var13,1,
	movl $1, -80(%ebp)
	
#callint,var14,label1,var12,var13,
	pushl -80(%ebp)
	pushl -76(%ebp)
	call label1
	addl $8, %esp
	movl %eax, -84(%ebp)
	
#restore_registers,
	
#retint,var14,
	movl -84(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#goto,label5,
	jmp label5
	
#label,label4,

label4:

	
#label,label5,

label5:

	
#=,var15,0,
	movl $0, -44(%ebp)
	
#>,var16,var1,var15,
	movl -12(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setge %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -48(%ebp)
	
#=,var17,0,
	movl $0, -52(%ebp)
	
#>,var18,var0,var17,
	movl -4(%ebp), %eax
	movl -52(%ebp), %ebx
	cmp %eax, %ebx
	setge %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -56(%ebp)
	
#&&,var19,var16,var18,
	movl -48(%ebp), %eax
	movl -56(%ebp), %ebx
	and %eax, %ebx
	movl %ebx, -60(%ebp)
	
#ifgoto,var19,label6,
	movl -60(%ebp), %eax
	cmp $0, %eax
	je label6
	
#save_registers,
	
#=,var20,1,
	movl $1, -88(%ebp)
	
#-,var21,var1,var20,
	movl -12(%ebp), %eax
	movl -88(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -92(%ebp)
	
#save_registers,
	
#=,var22,1,
	movl $1, -96(%ebp)
	
#-,var23,var0,var22,
	movl -4(%ebp), %eax
	movl -96(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -100(%ebp)
	
#callint,var24,label1,var1,var23,
	pushl -100(%ebp)
	pushl -12(%ebp)
	call label1
	addl $8, %esp
	movl %eax, -104(%ebp)
	
#restore_registers,
	
#callint,var25,label1,var21,var24,
	pushl -104(%ebp)
	pushl -92(%ebp)
	call label1
	addl $8, %esp
	movl %eax, -108(%ebp)
	
#restore_registers,
	
#retint,var25,
	movl -108(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#goto,label7,
	jmp label7
	
#label,label6,

label6:

	
#label,label7,

label7:

	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $24, %esp
	
#scan,var26,
	lea -4(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var27,
	lea -12(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#save_registers,
	
#callint,var28,label1,var26,var27,
	pushl -12(%ebp)
	pushl -4(%ebp)
	call label1
	addl $8, %esp
	movl %eax, -16(%ebp)
	
#restore_registers,
	
#print,var28,
	push -16(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#=,var29,0,
	movl $0, -20(%ebp)
	
#retint,var29,
	movl -20(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
