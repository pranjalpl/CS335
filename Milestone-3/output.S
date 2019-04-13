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
	
#=,var7,2,
	movl $2, -44(%ebp)
	
#=,var9,3,
	movl $3, -56(%ebp)
	
#=,var11,4,
	movl $4, -68(%ebp)
	
#=,var13,10,
	movl $10, -80(%ebp)
	
#=,var15,12,
	movl $12, -92(%ebp)
	
#=,var17,1,
	movl $1, -104(%ebp)
	
#=,var19,1,
	movl $1, -116(%ebp)
	
#=,var21,1,
	movl $1, -128(%ebp)
	
#=,var23,0,
	movl $0, -140(%ebp)
	
#=,var25,0,
	movl $0, -152(%ebp)
	
#=,var13,var21,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label2,

label2:

	
#<=,var26,var13,var7,
	movl -80(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -156(%ebp)
	
#=,var28,var26,
	movl -156(%ebp), %eax
	movl %eax, -164(%ebp)
	
#=,var29,1,
	movl $1, -168(%ebp)
	
#-,var28,var29,var28,
	movl -168(%ebp), %eax
	movl -164(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -164(%ebp)
	
#ifgoto,var28,label3,
	movl -164(%ebp), %eax
	cmp $0, %eax
	je label3
	
#=,var17,var21,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label4,

label4:

	
#<=,var30,var17,var7,
	movl -104(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -172(%ebp)
	
#=,var32,var30,
	movl -172(%ebp), %eax
	movl %eax, -180(%ebp)
	
#=,var33,1,
	movl $1, -184(%ebp)
	
#-,var32,var33,var32,
	movl -184(%ebp), %eax
	movl -180(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -180(%ebp)
	
#ifgoto,var32,label5,
	movl -180(%ebp), %eax
	cmp $0, %eax
	je label5
	
#=,var19,var21,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label6,

label6:

	
#<=,var34,var19,var7,
	movl -116(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -188(%ebp)
	
#=,var36,var34,
	movl -188(%ebp), %eax
	movl %eax, -196(%ebp)
	
#=,var37,1,
	movl $1, -200(%ebp)
	
#-,var36,var37,var36,
	movl -200(%ebp), %eax
	movl -196(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -196(%ebp)
	
#ifgoto,var36,label7,
	movl -196(%ebp), %eax
	cmp $0, %eax
	je label7
	
#=,var38,1,
	movl $1, -204(%ebp)
	
#+,var39,var23,var38,
	movl -140(%ebp), %eax
	movl -204(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -208(%ebp)
	
#=,var23,var39,
	movl -208(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var35,var19,var21,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -192(%ebp)
	
#=,var19,var35,
	movl -192(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label6,
	jmp label6
	
#label,label7,

label7:

	
#+,var31,var17,var21,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -176(%ebp)
	
#=,var17,var31,
	movl -176(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label4,
	jmp label4
	
#label,label5,

label5:

	
#+,var27,var13,var21,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -160(%ebp)
	
#=,var13,var27,
	movl -160(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label2,
	jmp label2
	
#label,label3,

label3:

	
#=,var13,var21,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label8,

label8:

	
#<=,var40,var13,var9,
	movl -80(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -212(%ebp)
	
#=,var42,var40,
	movl -212(%ebp), %eax
	movl %eax, -220(%ebp)
	
#=,var43,1,
	movl $1, -224(%ebp)
	
#-,var42,var43,var42,
	movl -224(%ebp), %eax
	movl -220(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -220(%ebp)
	
#ifgoto,var42,label9,
	movl -220(%ebp), %eax
	cmp $0, %eax
	je label9
	
#=,var17,var21,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label10,

label10:

	
#<=,var44,var17,var9,
	movl -104(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -228(%ebp)
	
#=,var46,var44,
	movl -228(%ebp), %eax
	movl %eax, -236(%ebp)
	
#=,var47,1,
	movl $1, -240(%ebp)
	
#-,var46,var47,var46,
	movl -240(%ebp), %eax
	movl -236(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -236(%ebp)
	
#ifgoto,var46,label11,
	movl -236(%ebp), %eax
	cmp $0, %eax
	je label11
	
#=,var19,var21,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label12,

label12:

	
#<=,var48,var19,var9,
	movl -116(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -244(%ebp)
	
#=,var50,var48,
	movl -244(%ebp), %eax
	movl %eax, -252(%ebp)
	
#=,var51,1,
	movl $1, -256(%ebp)
	
#-,var50,var51,var50,
	movl -256(%ebp), %eax
	movl -252(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -252(%ebp)
	
#ifgoto,var50,label13,
	movl -252(%ebp), %eax
	cmp $0, %eax
	je label13
	
#=,var52,1,
	movl $1, -260(%ebp)
	
#+,var53,var23,var52,
	movl -140(%ebp), %eax
	movl -260(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -264(%ebp)
	
#=,var23,var53,
	movl -264(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var49,var19,var21,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -248(%ebp)
	
#=,var19,var49,
	movl -248(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label12,
	jmp label12
	
#label,label13,

label13:

	
#+,var45,var17,var21,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -232(%ebp)
	
#=,var17,var45,
	movl -232(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label10,
	jmp label10
	
#label,label11,

label11:

	
#+,var41,var13,var21,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -216(%ebp)
	
#=,var13,var41,
	movl -216(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label8,
	jmp label8
	
#label,label9,

label9:

	
#=,var13,var21,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label14,

label14:

	
#<=,var54,var13,var11,
	movl -80(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -268(%ebp)
	
#=,var56,var54,
	movl -268(%ebp), %eax
	movl %eax, -276(%ebp)
	
#=,var57,1,
	movl $1, -280(%ebp)
	
#-,var56,var57,var56,
	movl -280(%ebp), %eax
	movl -276(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -276(%ebp)
	
#ifgoto,var56,label15,
	movl -276(%ebp), %eax
	cmp $0, %eax
	je label15
	
#=,var17,var21,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label16,

label16:

	
#<=,var58,var17,var11,
	movl -104(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -284(%ebp)
	
#=,var60,var58,
	movl -284(%ebp), %eax
	movl %eax, -292(%ebp)
	
#=,var61,1,
	movl $1, -296(%ebp)
	
#-,var60,var61,var60,
	movl -296(%ebp), %eax
	movl -292(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -292(%ebp)
	
#ifgoto,var60,label17,
	movl -292(%ebp), %eax
	cmp $0, %eax
	je label17
	
#=,var19,var21,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label18,

label18:

	
#<=,var62,var19,var11,
	movl -116(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -300(%ebp)
	
#=,var64,var62,
	movl -300(%ebp), %eax
	movl %eax, -308(%ebp)
	
#=,var65,1,
	movl $1, -312(%ebp)
	
#-,var64,var65,var64,
	movl -312(%ebp), %eax
	movl -308(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -308(%ebp)
	
#ifgoto,var64,label19,
	movl -308(%ebp), %eax
	cmp $0, %eax
	je label19
	
#=,var66,1,
	movl $1, -316(%ebp)
	
#+,var67,var23,var66,
	movl -140(%ebp), %eax
	movl -316(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -320(%ebp)
	
#=,var23,var67,
	movl -320(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var63,var19,var21,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -304(%ebp)
	
#=,var19,var63,
	movl -304(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label18,
	jmp label18
	
#label,label19,

label19:

	
#+,var59,var17,var21,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -288(%ebp)
	
#=,var17,var59,
	movl -288(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label16,
	jmp label16
	
#label,label17,

label17:

	
#+,var55,var13,var21,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -272(%ebp)
	
#=,var13,var55,
	movl -272(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label14,
	jmp label14
	
#label,label15,

label15:

	
#print,var23,
	pushl %eax
	pushl %ecx
	pushl %edx
	pushl -140(%ebp)
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
