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
	sub $256, %esp
	
#pop-param,2,var2,
	movl 16(%ebp), %eax
	movl %eax, -20(%ebp)
	
#pop-param,1,var1,
	movl 12(%ebp), %eax
	movl %eax, -12(%ebp)
	
#pop-param,0,var0,
	movl 8(%ebp), %eax
	movl %eax, -4(%ebp)
	
#=,var4,4,
	movl $4, -32(%ebp)
	
#*,var5,var4,var2,
	movl -32(%ebp), %eax
	movl -20(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -36(%ebp)
	
#+,var6,var0,var5,
	movl -4(%ebp), %eax
	movl -36(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -40(%ebp)
	
#valueAtAddr,var7,var6,
	movl -40(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -44(%ebp)
	
#=,var3,var7,
	movl -44(%ebp), %eax
	movl %eax, -28(%ebp)
	
#=,var9,1,
	movl $1, -56(%ebp)
	
#-,var10,var1,var9,
	movl -12(%ebp), %eax
	movl -56(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -60(%ebp)
	
#=,var8,var10,
	movl -60(%ebp), %eax
	movl %eax, -52(%ebp)
	
#=,var12,var1,
	movl -12(%ebp), %eax
	movl %eax, -76(%ebp)
	
#label,label2,

label2:

	
#<,var13,var12,var2,
	movl -76(%ebp), %eax
	movl -20(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -168(%ebp)
	
#ifgoto,var13,label3,
	movl -168(%ebp), %eax
	cmp $0, %eax
	je label3
	
#=,var14,4,
	movl $4, -172(%ebp)
	
#*,var15,var14,var12,
	movl -172(%ebp), %eax
	movl -76(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -176(%ebp)
	
#+,var16,var0,var15,
	movl -4(%ebp), %eax
	movl -176(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -180(%ebp)
	
#valueAtAddr,var17,var16,
	movl -180(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -184(%ebp)
	
#<=,var18,var17,var7,
	movl -184(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -188(%ebp)
	
#ifgoto,var18,label4,
	movl -188(%ebp), %eax
	cmp $0, %eax
	je label4
	
#++,var10,
	incl -60(%ebp)
	
#=,var19,4,
	movl $4, -192(%ebp)
	
#*,var20,var19,var10,
	movl -192(%ebp), %eax
	movl -60(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -196(%ebp)
	
#+,var21,var0,var20,
	movl -4(%ebp), %eax
	movl -196(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -200(%ebp)
	
#valueAtAddr,var22,var21,
	movl -200(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -204(%ebp)
	
#=,var11,var22,
	movl -204(%ebp), %eax
	movl %eax, -68(%ebp)
	
#=,var23,4,
	movl $4, -208(%ebp)
	
#*,var24,var23,var10,
	movl -208(%ebp), %eax
	movl -60(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -212(%ebp)
	
#+,var25,var0,var24,
	movl -4(%ebp), %eax
	movl -212(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -216(%ebp)
	
#valueAtAddr,var26,var25,
	movl -216(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -220(%ebp)
	
#=,var27,4,
	movl $4, -224(%ebp)
	
#*,var28,var27,var12,
	movl -224(%ebp), %eax
	movl -76(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -228(%ebp)
	
#+,var29,var0,var28,
	movl -4(%ebp), %eax
	movl -228(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -232(%ebp)
	
#valueAtAddr,var30,var29,
	movl -232(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -236(%ebp)
	
#=,var26,var30,
	movl -236(%ebp), %eax
	movl %eax, -220(%ebp)
	
#store,var25,var26,
	movl -216(%ebp), %eax
	movl -220(%ebp), %ebx
	movl %ebx, (%eax)
	
#=,var31,4,
	movl $4, -240(%ebp)
	
#*,var32,var31,var12,
	movl -240(%ebp), %eax
	movl -76(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -244(%ebp)
	
#+,var33,var0,var32,
	movl -4(%ebp), %eax
	movl -244(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -248(%ebp)
	
#valueAtAddr,var34,var33,
	movl -248(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -252(%ebp)
	
#=,var34,var11,
	movl -68(%ebp), %eax
	movl %eax, -252(%ebp)
	
#store,var33,var34,
	movl -248(%ebp), %eax
	movl -252(%ebp), %ebx
	movl %ebx, (%eax)
	
#goto,label5,
	jmp label5
	
#label,label4,

label4:

	
#label,label5,

label5:

	
#++,var12,
	incl -76(%ebp)
	
#goto,label2,
	jmp label2
	
#label,label3,

label3:

	
#=,var35,4,
	movl $4, -80(%ebp)
	
#=,var36,1,
	movl $1, -84(%ebp)
	
#+,var37,var10,var36,
	movl -60(%ebp), %eax
	movl -84(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -88(%ebp)
	
#*,var38,var35,var37,
	movl -80(%ebp), %eax
	movl -88(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -92(%ebp)
	
#+,var39,var0,var38,
	movl -4(%ebp), %eax
	movl -92(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -96(%ebp)
	
#valueAtAddr,var40,var39,
	movl -96(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -100(%ebp)
	
#=,var11,var40,
	movl -100(%ebp), %eax
	movl %eax, -68(%ebp)
	
#=,var41,4,
	movl $4, -104(%ebp)
	
#=,var42,1,
	movl $1, -108(%ebp)
	
#+,var43,var10,var42,
	movl -60(%ebp), %eax
	movl -108(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -112(%ebp)
	
#*,var44,var41,var43,
	movl -104(%ebp), %eax
	movl -112(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -116(%ebp)
	
#+,var45,var0,var44,
	movl -4(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -120(%ebp)
	
#valueAtAddr,var46,var45,
	movl -120(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -124(%ebp)
	
#=,var47,4,
	movl $4, -128(%ebp)
	
#*,var48,var47,var2,
	movl -128(%ebp), %eax
	movl -20(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -132(%ebp)
	
#+,var49,var0,var48,
	movl -4(%ebp), %eax
	movl -132(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -136(%ebp)
	
#valueAtAddr,var50,var49,
	movl -136(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -140(%ebp)
	
#=,var46,var50,
	movl -140(%ebp), %eax
	movl %eax, -124(%ebp)
	
#store,var45,var46,
	movl -120(%ebp), %eax
	movl -124(%ebp), %ebx
	movl %ebx, (%eax)
	
#=,var51,4,
	movl $4, -144(%ebp)
	
#*,var52,var51,var2,
	movl -144(%ebp), %eax
	movl -20(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -148(%ebp)
	
#+,var53,var0,var52,
	movl -4(%ebp), %eax
	movl -148(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -152(%ebp)
	
#valueAtAddr,var54,var53,
	movl -152(%ebp), %eax
	movl 0(%eax), %ebx
	movl %ebx, -156(%ebp)
	
#=,var54,var11,
	movl -68(%ebp), %eax
	movl %eax, -156(%ebp)
	
#store,var53,var54,
	movl -152(%ebp), %eax
	movl -156(%ebp), %ebx
	movl %ebx, (%eax)
	
#=,var55,1,
	movl $1, -160(%ebp)
	
#+,var56,var10,var55,
	movl -60(%ebp), %eax
	movl -160(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -164(%ebp)
	
#retint,var56,
	movl -164(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#label6:,

label6:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $68, %esp
	
#pop-param,2,var59,
	movl 16(%ebp), %eax
	movl %eax, -20(%ebp)
	
#pop-param,1,var58,
	movl 12(%ebp), %eax
	movl %eax, -12(%ebp)
	
#pop-param,0,var57,
	movl 8(%ebp), %eax
	movl %eax, -4(%ebp)
	
#<,var60,var58,var59,
	movl -12(%ebp), %eax
	movl -20(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -24(%ebp)
	
#ifgoto,var60,label7,
	movl -24(%ebp), %eax
	cmp $0, %eax
	je label7
	
#save_registers,
	
#callint,var62,label1,var57,var58,var59,
	pushl -20(%ebp)
	pushl -12(%ebp)
	pushl -4(%ebp)
	call label1
	addl $12, %esp
	movl %eax, -40(%ebp)
	
#restore_registers,
	
#=,var61,var62,
	movl -40(%ebp), %eax
	movl %eax, -36(%ebp)
	
#save_registers,
	
#=,var63,1,
	movl $1, -44(%ebp)
	
#-,var64,var62,var63,
	movl -40(%ebp), %eax
	movl -44(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -48(%ebp)
	
#callint,var65,label6,var57,var58,var64,
	pushl -48(%ebp)
	pushl -12(%ebp)
	pushl -4(%ebp)
	call label6
	addl $12, %esp
	movl %eax, -52(%ebp)
	
#restore_registers,
	
#save_registers,
	
#=,var66,1,
	movl $1, -56(%ebp)
	
#+,var67,var62,var66,
	movl -40(%ebp), %eax
	movl -56(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -60(%ebp)
	
#callint,var68,label6,var57,var67,var59,
	pushl -20(%ebp)
	pushl -60(%ebp)
	pushl -4(%ebp)
	call label6
	addl $12, %esp
	movl %eax, -64(%ebp)
	
#restore_registers,
	
#goto,label8,
	jmp label8
	
#label,label7,

label7:

	
#label,label8,

label8:

	
#=,var69,1,
	movl $1, -28(%ebp)
	
#retint,var69,
	movl -28(%ebp), %eax
	movl %ebp, %esp
	pop %ebp
	ret
	
#label0:,

label0:

	# Function Prologue
	pushl %ebp
	movl %esp,  %ebp
	sub $136, %esp
	
#=,var73,0,
	movl $0, -80(%ebp)
	
#=,var72,var73,
	movl -80(%ebp), %eax
	movl %eax, -60(%ebp)
	
#label,label10,

label10:

	
#=,var74,10,
	movl $10, -84(%ebp)
	
#<,var75,var72,var74,
	movl -60(%ebp), %eax
	movl -84(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -88(%ebp)
	
#ifgoto,var75,label11,
	movl -88(%ebp), %eax
	cmp $0, %eax
	je label11
	
#scan,var71,
	lea -52(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#=,var76,4,
	movl $4, -92(%ebp)
	
#*,var77,var72,var76,
	movl -60(%ebp), %eax
	movl -92(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -96(%ebp)
	
#addr+,var78,var70,var77,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -96(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -100(%ebp)
	
#deref,var79,var78,
	movl -100(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -104(%ebp)
	
#=,var79,var71,
	movl -52(%ebp), %eax
	movl %eax, -104(%ebp)
	
#store,var78,var79,
	movl -100(%ebp), %eax
	movl -104(%ebp), %ebx
	movl %ebx, (%eax)
	
#++,var72,
	incl -60(%ebp)
	
#goto,label10,
	jmp label10
	
#label,label11,

label11:

	
#save_registers,
	
#addressOf,var80,var70,
	movl %ebp, %eax
	movl $4, %ebx
	subl %ebx, %eax
	movl %eax, -64(%ebp)
	
#=,var81,0,
	movl $0, -68(%ebp)
	
#=,var82,9,
	movl $9, -72(%ebp)
	
#callint,var83,label6,var80,var81,var82,
	pushl -72(%ebp)
	pushl -68(%ebp)
	pushl -64(%ebp)
	call label6
	addl $12, %esp
	movl %eax, -76(%ebp)
	
#restore_registers,
	
#=,var84,0,
	movl $0, -108(%ebp)
	
#=,var72,var84,
	movl -108(%ebp), %eax
	movl %eax, -60(%ebp)
	
#label,label12,

label12:

	
#=,var85,10,
	movl $10, -112(%ebp)
	
#<,var86,var72,var85,
	movl -60(%ebp), %eax
	movl -112(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -116(%ebp)
	
#ifgoto,var86,label13,
	movl -116(%ebp), %eax
	cmp $0, %eax
	je label13
	
#=,var87,4,
	movl $4, -120(%ebp)
	
#*,var88,var72,var87,
	movl -60(%ebp), %eax
	movl -120(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -124(%ebp)
	
#addr+,var89,var70,var88,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -124(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -128(%ebp)
	
#deref,var90,var89,
	movl -128(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -132(%ebp)
	
#print,var90,
	push -132(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#++,var72,
	incl -60(%ebp)
	
#goto,label12,
	jmp label12
	
#label,label13,

label13:


exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
