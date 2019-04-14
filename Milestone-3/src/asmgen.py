from ourparser import *

f = open('output.S', 'w')

def initializeGlobals():
    symbolList = scopeDict[0].globalSymbolList
    f.write('.data\n\n')
    for x in symbolList:
        if scopeDict[0].table[x]["type"] == "int_t":
            f.write( x +":\n\t.int\t0\n")
    f.write('outFormatInt:\n\t.string\t"%d\\n"\n')
    f.write('outFormatStr:\n\t.string\t"%s\\n"\n')
    f.write('inFormat:\n\t.string\t"%d"\n')
    f.write('\n.text\n\n.global main\n\nmain:\n\n')
    genInstr("call mainDriver")
    genInstr("jmp exit")
    f.write('\n\nmainDriver:\n\n')
    #genInstr('pushl %ebp')
    #genInstr('movl %esp, %ebp')


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
