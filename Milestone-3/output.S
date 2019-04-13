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
	
#=,var11,14,
	movl $14, -68(%ebp)
	
#=,var13,12,
	movl $12, -80(%ebp)
	
#=,var15,1,
	movl $1, -92(%ebp)
	
#=,var17,1,
	movl $1, -104(%ebp)
	
#=,var19,1,
	movl $1, -116(%ebp)
	
#=,var21,0,
	movl $0, -128(%ebp)
	
#=,var23,0,
	movl $0, -140(%ebp)
	
#=,var11,var19,
	movl -116(%ebp), %eax
	movl %eax, -68(%ebp)
	
#label,label2,

label2:

	
#<=,var24,var11,var7,
	movl -68(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -240(%ebp)
	
#=,var26,var24,
	movl -240(%ebp), %eax
	movl %eax, -248(%ebp)
	
#=,var27,1,
	movl $1, -252(%ebp)
	
#-,var26,var27,var26,
	movl -252(%ebp), %eax
	movl -248(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -248(%ebp)
	
#ifgoto,var26,label3,
	movl -248(%ebp), %eax
	cmp $0, %eax
	je label3
	
#=,var15,var19,
	movl -116(%ebp), %eax
	movl %eax, -92(%ebp)
	
#label,label4,

label4:

	
#<=,var28,var15,var7,
	movl -92(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -352(%ebp)
	
#=,var30,var28,
	movl -352(%ebp), %eax
	movl %eax, -360(%ebp)
	
#=,var31,1,
	movl $1, -364(%ebp)
	
#-,var30,var31,var30,
	movl -364(%ebp), %eax
	movl -360(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -360(%ebp)
	
#ifgoto,var30,label5,
	movl -360(%ebp), %eax
	cmp $0, %eax
	je label5
	
#=,var17,var19,
	movl -116(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label6,

label6:

	
#<=,var32,var17,var7,
	movl -104(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -464(%ebp)
	
#=,var34,var32,
	movl -464(%ebp), %eax
	movl %eax, -472(%ebp)
	
#=,var35,1,
	movl $1, -476(%ebp)
	
#-,var34,var35,var34,
	movl -476(%ebp), %eax
	movl -472(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -472(%ebp)
	
#ifgoto,var34,label7,
	movl -472(%ebp), %eax
	cmp $0, %eax
	je label7
	
#=,var36,1,
	movl $1, -480(%ebp)
	
#+,var37,var21,var36,
	movl -128(%ebp), %eax
	movl -480(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -484(%ebp)
	
#=,var21,var37,
	movl -484(%ebp), %eax
	movl %eax, -128(%ebp)
	
#+,var33,var17,var19,
	movl -104(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -468(%ebp)
	
#=,var17,var33,
	movl -468(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label6,
	jmp label6
	
#label,label7,

label7:

	
#+,var29,var15,var19,
	movl -92(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -356(%ebp)
	
#=,var15,var29,
	movl -356(%ebp), %eax
	movl %eax, -92(%ebp)
	
#goto,label4,
	jmp label4
	
#label,label5,

label5:

	
#+,var25,var11,var19,
	movl -68(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -244(%ebp)
	
#=,var11,var25,
	movl -244(%ebp), %eax
	movl %eax, -68(%ebp)
	
#goto,label2,
	jmp label2
	
#label,label3,

label3:

	
#=,var11,var19,
	movl -116(%ebp), %eax
	movl %eax, -68(%ebp)
	
#label,label8,

label8:

	
#<=,var38,var11,var9,
	movl -68(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -584(%ebp)
	
#=,var40,var38,
	movl -584(%ebp), %eax
	movl %eax, -592(%ebp)
	
#=,var41,1,
	movl $1, -596(%ebp)
	
#-,var40,var41,var40,
	movl -596(%ebp), %eax
	movl -592(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -592(%ebp)
	
#ifgoto,var40,label9,
	movl -592(%ebp), %eax
	cmp $0, %eax
	je label9
	
#=,var15,var19,
	movl -116(%ebp), %eax
	movl %eax, -92(%ebp)
	
#label,label10,

label10:

	
#<=,var42,var15,var9,
	movl -92(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -696(%ebp)
	
#=,var44,var42,
	movl -696(%ebp), %eax
	movl %eax, -704(%ebp)
	
#=,var45,1,
	movl $1, -708(%ebp)
	
#-,var44,var45,var44,
	movl -708(%ebp), %eax
	movl -704(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -704(%ebp)
	
#ifgoto,var44,label11,
	movl -704(%ebp), %eax
	cmp $0, %eax
	je label11
	
#=,var17,var19,
	movl -116(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label12,

label12:

	
#<=,var46,var17,var9,
	movl -104(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -808(%ebp)
	
#=,var48,var46,
	movl -808(%ebp), %eax
	movl %eax, -816(%ebp)
	
#=,var49,1,
	movl $1, -820(%ebp)
	
#-,var48,var49,var48,
	movl -820(%ebp), %eax
	movl -816(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -816(%ebp)
	
#ifgoto,var48,label13,
	movl -816(%ebp), %eax
	cmp $0, %eax
	je label13
	
#=,var50,1,
	movl $1, -824(%ebp)
	
#+,var51,var21,var50,
	movl -128(%ebp), %eax
	movl -824(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -828(%ebp)
	
#=,var21,var51,
	movl -828(%ebp), %eax
	movl %eax, -128(%ebp)
	
#+,var47,var17,var19,
	movl -104(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -812(%ebp)
	
#=,var17,var47,
	movl -812(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label12,
	jmp label12
	
#label,label13,

label13:

	
#+,var43,var15,var19,
	movl -92(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -700(%ebp)
	
#=,var15,var43,
	movl -700(%ebp), %eax
	movl %eax, -92(%ebp)
	
#goto,label10,
	jmp label10
	
#label,label11,

label11:

	
#+,var39,var11,var19,
	movl -68(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -588(%ebp)
	
#=,var11,var39,
	movl -588(%ebp), %eax
	movl %eax, -68(%ebp)
	
#goto,label8,
	jmp label8
	
#label,label9,

label9:

	
#=,var11,var19,
	movl -116(%ebp), %eax
	movl %eax, -68(%ebp)
	
#label,label14,

label14:

	
#<=,var52,var11,var9,
	movl -68(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -928(%ebp)
	
#=,var54,var52,
	movl -928(%ebp), %eax
	movl %eax, -936(%ebp)
	
#=,var55,1,
	movl $1, -940(%ebp)
	
#-,var54,var55,var54,
	movl -940(%ebp), %eax
	movl -936(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -936(%ebp)
	
#ifgoto,var54,label15,
	movl -936(%ebp), %eax
	cmp $0, %eax
	je label15
	
#=,var15,var19,
	movl -116(%ebp), %eax
	movl %eax, -92(%ebp)
	
#label,label16,

label16:

	
#<=,var56,var15,var9,
	movl -92(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -1040(%ebp)
	
#=,var58,var56,
	movl -1040(%ebp), %eax
	movl %eax, -1048(%ebp)
	
#=,var59,1,
	movl $1, -1052(%ebp)
	
#-,var58,var59,var58,
	movl -1052(%ebp), %eax
	movl -1048(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -1048(%ebp)
	
#ifgoto,var58,label17,
	movl -1048(%ebp), %eax
	cmp $0, %eax
	je label17
	
#=,var17,var19,
	movl -116(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label18,

label18:

	
#<=,var60,var17,var9,
	movl -104(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -1152(%ebp)
	
#=,var62,var60,
	movl -1152(%ebp), %eax
	movl %eax, -1160(%ebp)
	
#=,var63,1,
	movl $1, -1164(%ebp)
	
#-,var62,var63,var62,
	movl -1164(%ebp), %eax
	movl -1160(%ebp), %ebx
	subl %eax, %ebx
	movl %ebx, -1160(%ebp)
	
#ifgoto,var62,label19,
	movl -1160(%ebp), %eax
	cmp $0, %eax
	je label19
	
#=,var64,1,
	movl $1, -1168(%ebp)
	
#+,var65,var21,var64,
	movl -128(%ebp), %eax
	movl -1168(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -1172(%ebp)
	
#=,var21,var65,
	movl -1172(%ebp), %eax
	movl %eax, -128(%ebp)
	
#+,var61,var17,var19,
	movl -104(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -1156(%ebp)
	
#=,var17,var61,
	movl -1156(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label18,
	jmp label18
	
#label,label19,

label19:

	
#+,var57,var15,var19,
	movl -92(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -1044(%ebp)
	
#=,var15,var57,
	movl -1044(%ebp), %eax
	movl %eax, -92(%ebp)
	
#goto,label16,
	jmp label16
	
#label,label17,

label17:

	
#+,var53,var11,var19,
	movl -68(%ebp), %eax
	movl -116(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -932(%ebp)
	
#=,var11,var53,
	movl -932(%ebp), %eax
	movl %eax, -68(%ebp)
	
#goto,label14,
	jmp label14
	
#label,label15,

label15:

	
#print,var21,
	pushl %eax
	pushl %ecx
	pushl %edx
	pushl -128(%ebp)
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
