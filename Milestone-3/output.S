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
	sub $436, %esp
	
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
	subl %ebx, %eax
	movl %eax, -164(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -180(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -196(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -220(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -236(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -252(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -276(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -292(%ebp)
	
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
	subl %ebx, %eax
	movl %eax, -308(%ebp)
	
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

	
#=,var13,var21,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label20,

label20:

	
#<=,var68,var13,var9,
	movl -80(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -324(%ebp)
	
#=,var70,var68,
	movl -324(%ebp), %eax
	movl %eax, -332(%ebp)
	
#=,var71,1,
	movl $1, -336(%ebp)
	
#-,var70,var71,var70,
	movl -336(%ebp), %eax
	movl -332(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -332(%ebp)
	
#ifgoto,var70,label21,
	movl -332(%ebp), %eax
	cmp $0, %eax
	je label21
	
#=,var17,var21,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label22,

label22:

	
#<=,var72,var17,var9,
	movl -104(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -340(%ebp)
	
#=,var74,var72,
	movl -340(%ebp), %eax
	movl %eax, -348(%ebp)
	
#=,var75,1,
	movl $1, -352(%ebp)
	
#-,var74,var75,var74,
	movl -352(%ebp), %eax
	movl -348(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -348(%ebp)
	
#ifgoto,var74,label23,
	movl -348(%ebp), %eax
	cmp $0, %eax
	je label23
	
#=,var19,var21,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label24,

label24:

	
#<=,var76,var19,var9,
	movl -116(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -356(%ebp)
	
#=,var78,var76,
	movl -356(%ebp), %eax
	movl %eax, -364(%ebp)
	
#=,var79,1,
	movl $1, -368(%ebp)
	
#-,var78,var79,var78,
	movl -368(%ebp), %eax
	movl -364(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -364(%ebp)
	
#ifgoto,var78,label25,
	movl -364(%ebp), %eax
	cmp $0, %eax
	je label25
	
#=,var80,1,
	movl $1, -372(%ebp)
	
#+,var81,var23,var80,
	movl -140(%ebp), %eax
	movl -372(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -376(%ebp)
	
#=,var23,var81,
	movl -376(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var77,var19,var21,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -360(%ebp)
	
#=,var19,var77,
	movl -360(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label24,
	jmp label24
	
#label,label25,

label25:

	
#+,var73,var17,var21,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -344(%ebp)
	
#=,var17,var73,
	movl -344(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label22,
	jmp label22
	
#label,label23,

label23:

	
#+,var69,var13,var21,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -328(%ebp)
	
#=,var13,var69,
	movl -328(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label20,
	jmp label20
	
#label,label21,

label21:

	
#=,var13,var21,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label26,

label26:

	
#<=,var82,var13,var11,
	movl -80(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -380(%ebp)
	
#=,var84,var82,
	movl -380(%ebp), %eax
	movl %eax, -388(%ebp)
	
#=,var85,1,
	movl $1, -392(%ebp)
	
#-,var84,var85,var84,
	movl -392(%ebp), %eax
	movl -388(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -388(%ebp)
	
#ifgoto,var84,label27,
	movl -388(%ebp), %eax
	cmp $0, %eax
	je label27
	
#=,var17,var21,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label28,

label28:

	
#<=,var86,var17,var11,
	movl -104(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -396(%ebp)
	
#=,var88,var86,
	movl -396(%ebp), %eax
	movl %eax, -404(%ebp)
	
#=,var89,1,
	movl $1, -408(%ebp)
	
#-,var88,var89,var88,
	movl -408(%ebp), %eax
	movl -404(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -404(%ebp)
	
#ifgoto,var88,label29,
	movl -404(%ebp), %eax
	cmp $0, %eax
	je label29
	
#=,var19,var21,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label30,

label30:

	
#<=,var90,var19,var11,
	movl -116(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -412(%ebp)
	
#=,var92,var90,
	movl -412(%ebp), %eax
	movl %eax, -420(%ebp)
	
#=,var93,1,
	movl $1, -424(%ebp)
	
#-,var92,var93,var92,
	movl -424(%ebp), %eax
	movl -420(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -420(%ebp)
	
#ifgoto,var92,label31,
	movl -420(%ebp), %eax
	cmp $0, %eax
	je label31
	
#=,var94,1,
	movl $1, -428(%ebp)
	
#+,var95,var23,var94,
	movl -140(%ebp), %eax
	movl -428(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -432(%ebp)
	
#=,var23,var95,
	movl -432(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var91,var19,var21,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -416(%ebp)
	
#=,var19,var91,
	movl -416(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label30,
	jmp label30
	
#label,label31,

label31:

	
#+,var87,var17,var21,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -400(%ebp)
	
#=,var17,var87,
	movl -400(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label28,
	jmp label28
	
#label,label29,

label29:

	
#+,var83,var13,var21,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -384(%ebp)
	
#=,var13,var83,
	movl -384(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label26,
	jmp label26
	
#label,label27,

label27:

	
#print,var23,
	push -140(%ebp)
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
	sub $348, %esp
	
#=,var97,1,
	movl $1, -8(%ebp)
	
#=,var99,1,
	movl $1, -20(%ebp)
	
#=,var101,1,
	movl $1, -32(%ebp)
	
#=,var103,2,
	movl $2, -44(%ebp)
	
#=,var105,3,
	movl $3, -56(%ebp)
	
#=,var107,4,
	movl $4, -68(%ebp)
	
#=,var109,10,
	movl $10, -80(%ebp)
	
#=,var111,12,
	movl $12, -92(%ebp)
	
#=,var113,1,
	movl $1, -104(%ebp)
	
#=,var115,1,
	movl $1, -116(%ebp)
	
#=,var117,1,
	movl $1, -128(%ebp)
	
#=,var119,0,
	movl $0, -140(%ebp)
	
#=,var121,0,
	movl $0, -152(%ebp)
	
#=,var109,var117,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label33,

label33:

	
#=,var122,1,
	movl $1, -156(%ebp)
	
#+,var123,var103,var122,
	movl -44(%ebp), %eax
	movl -156(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -160(%ebp)
	
#!=,var124,var109,var123,
	movl -80(%ebp), %eax
	movl -160(%ebp), %ebx
	cmp %eax, %ebx
	sete %al
	movzbl %al, %eax
	movl %eax, -164(%ebp)
	
#=,var126,var124,
	movl -164(%ebp), %eax
	movl %eax, -172(%ebp)
	
#=,var127,1,
	movl $1, -176(%ebp)
	
#-,var126,var127,var126,
	movl -176(%ebp), %eax
	movl -172(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -172(%ebp)
	
#ifgoto,var126,label34,
	movl -172(%ebp), %eax
	cmp $0, %eax
	je label34
	
#=,var113,var117,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label35,

label35:

	
#<=,var128,var113,var103,
	movl -104(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -180(%ebp)
	
#=,var130,var128,
	movl -180(%ebp), %eax
	movl %eax, -188(%ebp)
	
#=,var131,1,
	movl $1, -192(%ebp)
	
#-,var130,var131,var130,
	movl -192(%ebp), %eax
	movl -188(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -188(%ebp)
	
#ifgoto,var130,label36,
	movl -188(%ebp), %eax
	cmp $0, %eax
	je label36
	
#=,var115,var117,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label37,

label37:

	
#<=,var132,var115,var103,
	movl -116(%ebp), %eax
	movl -44(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -196(%ebp)
	
#=,var134,var132,
	movl -196(%ebp), %eax
	movl %eax, -204(%ebp)
	
#=,var135,1,
	movl $1, -208(%ebp)
	
#-,var134,var135,var134,
	movl -208(%ebp), %eax
	movl -204(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -204(%ebp)
	
#ifgoto,var134,label38,
	movl -204(%ebp), %eax
	cmp $0, %eax
	je label38
	
#=,var136,1,
	movl $1, -212(%ebp)
	
#+,var137,var119,var136,
	movl -140(%ebp), %eax
	movl -212(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -216(%ebp)
	
#=,var119,var137,
	movl -216(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var133,var115,var117,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -200(%ebp)
	
#=,var115,var133,
	movl -200(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label37,
	jmp label37
	
#label,label38,

label38:

	
#+,var129,var113,var117,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -184(%ebp)
	
#=,var113,var129,
	movl -184(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label35,
	jmp label35
	
#label,label36,

label36:

	
#+,var125,var109,var117,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -168(%ebp)
	
#=,var109,var125,
	movl -168(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label33,
	jmp label33
	
#label,label34,

label34:

	
#print,var119,
	push -140(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#=,var109,var117,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label39,

label39:

	
#=,var138,1,
	movl $1, -220(%ebp)
	
#+,var139,var105,var138,
	movl -56(%ebp), %eax
	movl -220(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -224(%ebp)
	
#!=,var140,var109,var139,
	movl -80(%ebp), %eax
	movl -224(%ebp), %ebx
	cmp %eax, %ebx
	sete %al
	movzbl %al, %eax
	movl %eax, -228(%ebp)
	
#=,var142,var140,
	movl -228(%ebp), %eax
	movl %eax, -236(%ebp)
	
#=,var143,1,
	movl $1, -240(%ebp)
	
#-,var142,var143,var142,
	movl -240(%ebp), %eax
	movl -236(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -236(%ebp)
	
#ifgoto,var142,label40,
	movl -236(%ebp), %eax
	cmp $0, %eax
	je label40
	
#=,var113,var117,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label41,

label41:

	
#<=,var144,var113,var105,
	movl -104(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -244(%ebp)
	
#=,var146,var144,
	movl -244(%ebp), %eax
	movl %eax, -252(%ebp)
	
#=,var147,1,
	movl $1, -256(%ebp)
	
#-,var146,var147,var146,
	movl -256(%ebp), %eax
	movl -252(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -252(%ebp)
	
#ifgoto,var146,label42,
	movl -252(%ebp), %eax
	cmp $0, %eax
	je label42
	
#=,var115,var117,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label43,

label43:

	
#<=,var148,var115,var105,
	movl -116(%ebp), %eax
	movl -56(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -260(%ebp)
	
#=,var150,var148,
	movl -260(%ebp), %eax
	movl %eax, -268(%ebp)
	
#=,var151,1,
	movl $1, -272(%ebp)
	
#-,var150,var151,var150,
	movl -272(%ebp), %eax
	movl -268(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -268(%ebp)
	
#ifgoto,var150,label44,
	movl -268(%ebp), %eax
	cmp $0, %eax
	je label44
	
#=,var152,1,
	movl $1, -276(%ebp)
	
#+,var153,var119,var152,
	movl -140(%ebp), %eax
	movl -276(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -280(%ebp)
	
#=,var119,var153,
	movl -280(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var149,var115,var117,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -264(%ebp)
	
#=,var115,var149,
	movl -264(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label43,
	jmp label43
	
#label,label44,

label44:

	
#+,var145,var113,var117,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -248(%ebp)
	
#=,var113,var145,
	movl -248(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label41,
	jmp label41
	
#label,label42,

label42:

	
#+,var141,var109,var117,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -232(%ebp)
	
#=,var109,var141,
	movl -232(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label39,
	jmp label39
	
#label,label40,

label40:

	
#print,var119,
	push -140(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#=,var109,var117,
	movl -128(%ebp), %eax
	movl %eax, -80(%ebp)
	
#label,label45,

label45:

	
#=,var154,1,
	movl $1, -284(%ebp)
	
#+,var155,var107,var154,
	movl -68(%ebp), %eax
	movl -284(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -288(%ebp)
	
#!=,var156,var109,var155,
	movl -80(%ebp), %eax
	movl -288(%ebp), %ebx
	cmp %eax, %ebx
	sete %al
	movzbl %al, %eax
	movl %eax, -292(%ebp)
	
#=,var158,var156,
	movl -292(%ebp), %eax
	movl %eax, -300(%ebp)
	
#=,var159,1,
	movl $1, -304(%ebp)
	
#-,var158,var159,var158,
	movl -304(%ebp), %eax
	movl -300(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -300(%ebp)
	
#ifgoto,var158,label46,
	movl -300(%ebp), %eax
	cmp $0, %eax
	je label46
	
#=,var113,var117,
	movl -128(%ebp), %eax
	movl %eax, -104(%ebp)
	
#label,label47,

label47:

	
#<=,var160,var113,var107,
	movl -104(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -308(%ebp)
	
#=,var162,var160,
	movl -308(%ebp), %eax
	movl %eax, -316(%ebp)
	
#=,var163,1,
	movl $1, -320(%ebp)
	
#-,var162,var163,var162,
	movl -320(%ebp), %eax
	movl -316(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -316(%ebp)
	
#ifgoto,var162,label48,
	movl -316(%ebp), %eax
	cmp $0, %eax
	je label48
	
#=,var115,var117,
	movl -128(%ebp), %eax
	movl %eax, -116(%ebp)
	
#label,label49,

label49:

	
#<=,var164,var115,var107,
	movl -116(%ebp), %eax
	movl -68(%ebp), %ebx
	cmp %eax, %ebx
	setl %al
	movzbl %al, %eax
	movl %eax, -324(%ebp)
	
#=,var166,var164,
	movl -324(%ebp), %eax
	movl %eax, -332(%ebp)
	
#=,var167,1,
	movl $1, -336(%ebp)
	
#-,var166,var167,var166,
	movl -336(%ebp), %eax
	movl -332(%ebp), %ebx
	subl %ebx, %eax
	movl %eax, -332(%ebp)
	
#ifgoto,var166,label50,
	movl -332(%ebp), %eax
	cmp $0, %eax
	je label50
	
#=,var168,1,
	movl $1, -340(%ebp)
	
#+,var169,var119,var168,
	movl -140(%ebp), %eax
	movl -340(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -344(%ebp)
	
#=,var119,var169,
	movl -344(%ebp), %eax
	movl %eax, -140(%ebp)
	
#+,var165,var115,var117,
	movl -116(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -328(%ebp)
	
#=,var115,var165,
	movl -328(%ebp), %eax
	movl %eax, -116(%ebp)
	
#goto,label49,
	jmp label49
	
#label,label50,

label50:

	
#+,var161,var113,var117,
	movl -104(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -312(%ebp)
	
#=,var113,var161,
	movl -312(%ebp), %eax
	movl %eax, -104(%ebp)
	
#goto,label47,
	jmp label47
	
#label,label48,

label48:

	
#+,var157,var109,var117,
	movl -80(%ebp), %eax
	movl -128(%ebp), %ebx
	addl %eax, %ebx
	movl %ebx, -296(%ebp)
	
#=,var109,var157,
	movl -296(%ebp), %eax
	movl %eax, -80(%ebp)
	
#goto,label45,
	jmp label45
	
#label,label46,

label46:

	
#print,var119,
	push -140(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#retvoid,
	movl %ebp, %esp
	pop %ebp
	ret

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
