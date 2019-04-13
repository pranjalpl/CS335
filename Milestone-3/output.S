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
	sub $176, %esp
	
#=,var4,2,
	movl $2, -72(%ebp)
	
#=,var5,4,
	movl $4, -76(%ebp)
	
#*,var6,var4,var5,
	movl -72(%ebp), %eax
	movl -76(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -80(%ebp)
	
#addr+,var7,var0,var6,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -80(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -84(%ebp)
	
#deref,var8,var7,
	movl -84(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -88(%ebp)
	
#=,var9,100,
	movl $100, -92(%ebp)
	
#=,var8,var9,
	movl -92(%ebp), %eax
	movl %eax, -88(%ebp)
	
#store,var7,var8,
	movl -84(%ebp), %eax
	movl -88(%ebp), %ebx
	movl %ebx, (%eax)
	
#=,var10,3,
	movl $3, -96(%ebp)
	
#=,var11,4,
	movl $4, -100(%ebp)
	
#*,var12,var10,var11,
	movl -96(%ebp), %eax
	movl -100(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -104(%ebp)
	
#addr+,var13,var0,var12,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -104(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -108(%ebp)
	
#deref,var14,var13,
	movl -108(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -112(%ebp)
	
#=,var15,200,
	movl $200, -116(%ebp)
	
#=,var14,var15,
	movl -116(%ebp), %eax
	movl %eax, -112(%ebp)
	
#store,var13,var14,
	movl -108(%ebp), %eax
	movl -112(%ebp), %ebx
	movl %ebx, (%eax)
	
#=,var16,0,
	movl $0, -120(%ebp)
	
#=,var1,var16,
	movl -120(%ebp), %eax
	movl %eax, -52(%ebp)
	
#label,label2,

label2:

	
#=,var17,10,
	movl $10, -124(%ebp)
	
#<,var18,var1,var17,
	movl -52(%ebp), %eax
	movl -124(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -128(%ebp)
	
#ifgoto,var18,label3,
	movl -128(%ebp), %eax
	cmp $0, %eax
	je label3
	
#scan,var3,
	lea -68(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	addl $8, %esp
	
#=,var19,4,
	movl $4, -132(%ebp)
	
#*,var20,var1,var19,
	movl -52(%ebp), %eax
	movl -132(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -136(%ebp)
	
#addr+,var21,var0,var20,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -136(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -140(%ebp)
	
#deref,var22,var21,
	movl -140(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -144(%ebp)
	
#=,var22,var3,
	movl -68(%ebp), %eax
	movl %eax, -144(%ebp)
	
#store,var21,var22,
	movl -140(%ebp), %eax
	movl -144(%ebp), %ebx
	movl %ebx, (%eax)
	
#++,var1,
	incl -52(%ebp)
	
#goto,label2,
	jmp label2
	
#label,label3,

label3:

	
#=,var23,0,
	movl $0, -148(%ebp)
	
#=,var1,var23,
	movl -148(%ebp), %eax
	movl %eax, -52(%ebp)
	
#label,label4,

label4:

	
#=,var24,10,
	movl $10, -152(%ebp)
	
#<,var25,var1,var24,
	movl -52(%ebp), %eax
	movl -152(%ebp), %ebx
	cmp %eax, %ebx
	setle %al
	movzbl %al, %eax
	movl $1, %ecx
	subl %eax, %ecx
	movl %ecx, -156(%ebp)
	
#ifgoto,var25,label5,
	movl -156(%ebp), %eax
	cmp $0, %eax
	je label5
	
#=,var26,4,
	movl $4, -160(%ebp)
	
#*,var27,var1,var26,
	movl -52(%ebp), %eax
	movl -160(%ebp), %ebx
	imul %eax, %ebx
	movl %ebx, -164(%ebp)
	
#addr+,var28,var0,var27,
	movl $4, %eax
	movl %ebp, %ebx
	subl %eax, %ebx
	movl -164(%ebp), %ecx
	addl %ecx, %ebx
	movl %ebx, -168(%ebp)
	
#deref,var29,var28,
	movl -168(%ebp), %eax
	movl (%eax), %ebx
	movl %ebx, -172(%ebp)
	
#print,var29,
	push -172(%ebp)
	push $outFormatInt
	call printf
	addl $8, %esp
	
#++,var1,
	incl -52(%ebp)
	
#goto,label4,
	jmp label4
	
#label,label5,

label5:


exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
