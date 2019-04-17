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
	sub $92, %esp
	
#pop-param,7,var7,
	movl 36(%ebp), %eax
	movl %eax, -60(%ebp)
	
#pop-param,6,var6,
	movl 32(%ebp), %eax
	movl %eax, -52(%ebp)
	
#pop-param,5,var5,
	movl 28(%ebp), %eax
	movl %eax, -44(%ebp)
	
#pop-param,4,var4,
	movl 24(%ebp), %eax
	movl %eax, -36(%ebp)
	
#pop-param,3,var3,
	movl 20(%ebp), %eax
	movl %eax, -28(%ebp)
	
#pop-param,2,var2,
	movl 16(%ebp), %eax
	movl %eax, -20(%ebp)
	
#pop-param,1,var1,
	movl 12(%ebp), %eax
	movl %eax, -12(%ebp)
	
#pop-param,0,var0,
	movl 8(%ebp), %eax
	movl %eax, -4(%ebp)
	
#+,var8,var6,var7,
	movl -52(%ebp), %eax
	movl -60(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -64(%ebp)
	
#+,var9,var5,var8,
	movl -44(%ebp), %eax
	movl -64(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -68(%ebp)
	
#+,var10,var4,var9,
	movl -36(%ebp), %eax
	movl -68(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -72(%ebp)
	
#+,var11,var3,var10,
	movl -28(%ebp), %eax
	movl -72(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -76(%ebp)
	
#+,var12,var2,var11,
	movl -20(%ebp), %eax
	movl -76(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -80(%ebp)
	
#+,var13,var1,var12,
	movl -12(%ebp), %eax
	movl -80(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -84(%ebp)
	
#+,var14,var0,var13,
	movl -4(%ebp), %eax
	movl -84(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -88(%ebp)
	
#retint,var14,
	movl -88(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $68, %esp
	
#scan,var22,
	lea -60(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var15,
	lea -4(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var16,
	lea -12(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var17,
	lea -20(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var18,
	lea -28(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var19,
	lea -36(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var20,
	lea -44(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var21,
	lea -52(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#save_registers,
	
#callint,var23,label1,var22,var15,var16,var17,var18,var19,var20,var21,
	pushl -52(%ebp)
	pushl -44(%ebp)
	pushl -36(%ebp)
	pushl -28(%ebp)
	pushl -20(%ebp)
	pushl -12(%ebp)
	pushl -4(%ebp)
	pushl -60(%ebp)
	call label1
	addl $32, %esp
	movl %eax, -64(%ebp)
	
#restore_registers,
	
#print,var23,
	push -64(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
