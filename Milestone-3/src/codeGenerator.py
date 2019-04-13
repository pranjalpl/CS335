from ourparser import *
from asmgen import *
from utils import *

# Corresponds to 4 operand instructions
# x is multiply and * is dereference
type_4 = ['+', '-', 'x', '/', '%', '&', '|', '^', '==', '<', '>', '!=', '<=', '>=']
type_3 = ['=', '+=', '-=', 'x=', '&=',
          '|=', '^=', '<<=', '>>=', 'ifgoto', 'callint', 'load', 'store', 'array', 'pload', 'addr']
type_2 = ['++', '!', '--', 'label', 'printint', 'printstr', 'scan', 'callvoid', 'goto', 'retint', 'push', 'pop']
type_1 = ['retvoid']

instr_types = type_4 + type_3 + type_2 + type_1

addrDes = {}        # Address Descriptor
stack = []          # Stack of symbols to keep track of the function return variables, implemented through list.
regDes = {          # Register Descriptor
    'esp': None,
    'ebp': None,
    'eax': None,
    'ebx': None,
    'ecx': None,
    'edx': None,
    'esi': None,
    'edi': None
}

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

initializeGlobals()
scopeVarList = []
for i in range(0, len(scopeDict)):
    scopeVarList.append([])
    genVarListFromSymTable(scopeDict[0], scopeVarList[-1])

for instr in IR:
    if instr[0] == '+':
        op1offset = offsetOf(instr[2], varList)
        op2offset = offsetOf(instr[3], varList)
        destoffset = offsetOf(instr[1], varList)
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('addl %%eax, %%ebx')
        genInstr('movl %%eax, -%d(%%ebp)'%(destoffset))
    
    elif instr[0] == '-':
        op1offset = offsetOf(instr[2], varList)
        op2offset = offsetOf(instr[3], varList)
        destoffset = offsetOf(instr[1], varList)
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('subl %%eax, %%ebx')
        genInstr('movl %%eax, -%d(%%ebp)'%(destoffset))
    
    elif instr[0] == '=':
        destoffset = offsetOf(instr[1], varList)
        if str(instr[2]).startswith('var'):
            # srcoffset = 
            genInstr('movl $%d, -%d(%%ebp)'%(instr[2], destoffset))            
        else:
            genInstr('movl $%d, -%d(%%ebp)'%(instr[2], destoffset))
    
closeFile()