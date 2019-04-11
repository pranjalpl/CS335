from config import *

f = open('output.S', 'w')

def initializeGlobals():
    symbolList = ST.globalSymbolList
    f.write('.data\n\n')
    for x in symbolList:
        if ST.table[x]["type"] == "int":
            f.write( x +":\n\t.int\t0\n")
    f.write('outFormatInt:\n\t.asciz\t"%d\\n"\n')
    f.write('outFormatStr:\n\t.asciz\t"%s\\n"\n')
    f.write('inFormat:\n\t.ascii\t"%d"\n')
    f.write('\n.text\n\n.global main\n\nmain:\n\n')
    genInstr("call mainMandal")
    genInstr("jmp exit")
    f.write('\n\nmainMandal:\n\n')
    genInstr('pushl %ebp')
    genInstr('movl %esp, %ebp')


def genInstr(instr):
    f.write('\t' + instr + '\n')


def genLabel(label):
    f.write('\n' + label + ":\n\n")

def closeFile():
	# f.write('\\n')
        genLabel("exit")
        genInstr("movl $0, %ebx")
        genInstr("movl $1, %eax")
        genInstr("int $0x80")
        f.close()
