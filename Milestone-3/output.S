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
	sub $120, %esp
	
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
	
#print,var14,
	push -88(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#+,var15,var6,var7,
	movl -52(%ebp), %eax
	movl -60(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -92(%ebp)
	
#+,var16,var5,var15,
	movl -44(%ebp), %eax
	movl -92(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -96(%ebp)
	
#+,var17,var4,var16,
	movl -36(%ebp), %eax
	movl -96(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -100(%ebp)
	
#+,var18,var3,var17,
	movl -28(%ebp), %eax
	movl -100(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -104(%ebp)
	
#+,var19,var2,var18,
	movl -20(%ebp), %eax
	movl -104(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -108(%ebp)
	
#+,var20,var1,var19,
	movl -12(%ebp), %eax
	movl -108(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -112(%ebp)
	
#+,var21,var0,var20,
	movl -4(%ebp), %eax
	movl -112(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -116(%ebp)
	
#print,var21,
	push -116(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#retvoid,
	movl %ebp, %esp
	pop %ebp
	ret
	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $72, %esp
	
#scan,var29,
	lea -60(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var22,
	lea -4(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var23,
	lea -12(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var24,
	lea -20(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var25,
	lea -28(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var26,
	lea -36(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var27,
	lea -44(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#scan,var28,
	lea -52(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#=,var30,1,
	movl $1, -64(%ebp)
	
#print,var30,
	push -64(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#save_registers,
	
#callint,var31,label1,var29,var22,var23,var24,var25,var26,var27,var28,
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
	movl %eax, -68(%ebp)
	
#restore_registers,

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
