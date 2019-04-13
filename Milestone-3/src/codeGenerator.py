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
# offsets = get_offset(scopeDict)
offsets,no_use=get_offset(scopeDict)
for instr in IR:
    estr = '#'
    for i in instr:
        estr += str(i) + ','
    genInstr('\n'+estr)
    if instr[0] == '+':
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('addl %eax, %ebx')
        genInstr('movl %%ebx, -%d(%%ebp)'%(destoffset))
    
    elif instr[0] == '-':
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('subl %eax, %ebx')
        genInstr('movl %%ebx, -%d(%%ebp)'%(destoffset))

    elif instr[0] == '*':
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('imul %eax, %ebx')
        genInstr('movl %%ebx, -%d(%%ebp)'%(destoffset))
    
    elif instr[0] == '/':
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('idiv %ebx')
        genInstr('movl %%eax, -%d(%%ebp)'%(destoffset))

    elif instr[0] == '%':
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('idiv %ebx')
        genInstr('movl %%edx, -%d(%%ebp)'%(destoffset))
        
    elif instr[0] in ['&', '|', '^', '&&', '||']:
        op = 'and'
        if instr[0] == '|' or instr[0] == '||':
            op = 'or'
        elif instr[0] == '^':
            op = 'xor'
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('%s %%eax, %%ebx' % (op))
        genInstr('movl %%eax, -%d(%%ebp)'%(destoffset))
    
    elif instr[0] in ['<', '<=', '>', '>=', '==', '!=']:
        d = {
            '<': 'setle',
            '<=': 'setl',
            '>': 'setge',
            '>=': 'setg',
            '==': 'sete',
            '!=': 'setne',
        }
        op1offset = offsets[instr[2]]
        op2offset = offsets[instr[3]]
        destoffset = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax'%(op1offset))
        genInstr('movl -%d(%%ebp), %%ebx'%(op2offset))
        genInstr('cmp %eax, %ebx')
        genInstr('%s %%al' % (d[instr[0]]))
        genInstr('movzbl %al, %eax')
        # if not instr[0] in ['==', '!=']:
        #     genInstr('movl $1, %ecx')
        #     genInstr('subl %eax, %ecx')
        genInstr('movl %%eax, -%d(%%ebp)' % (destoffset))

    elif instr[0] == '=':
        print(instr)
        destoffset = offsets[instr[1]]
        print('got', destoffset)
        if str(instr[2]).startswith('var'):
            srcoffset = offsets[instr[2]]
            genInstr('movl -%d(%%ebp), %%eax' % (srcoffset))
            genInstr('movl %%eax, -%d(%%ebp)' % (destoffset))  
        else:
            genInstr('movl $%d, -%d(%%ebp)'%(int(instr[2]), destoffset))
    
    elif instr[0] == 'label':
        genLabel(instr[1])

    elif instr[0][-1] == ':':
        off = max_offsets[instr[0][:-1]]
        genLabel(instr[0][:-1])
        genInstr("# Function Prologue")
        genInstr("pushl %ebp")
        genInstr("movl %esp,  %ebp")
        genInstr("sub $%d, %%esp" % (off))    
    
    elif instr[0] == 'callint':
        params = instr[3:]
        for p in params[::-1]:
            offset = offsets[p]
            genInstr('pushl -%d(%%ebp)' % (offset))
        genInstr('call %s' % (instr[2]))
        # TODO Change this: Assuming 4 byte params
        genInstr('addl $%d, %%esp' % (4*len(params)))
        off = offsets[instr[1]]
        genInstr('movl %%eax, -%d(%%ebp)' % (off))
    
    elif instr[0] == 'pop-param':
        srcoff = instr[1] * 4 + 8
        destoff = offsets[instr[2]]
        genInstr("movl %d(%%ebp), %%eax" %(srcoff))
        genInstr("movl %%eax, -%d(%%ebp)" % (destoff))
    
    elif instr[0] == 'retvoid':
        genInstr('movl %ebp, %esp')
        genInstr('pop %ebp')
        genInstr('ret')

    elif instr[0] == 'retint':
        off = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax' % (off))
        genInstr('movl %ebp, %esp')
        genInstr('pop %ebp')
        genInstr('ret')

    elif instr[0] == 'print':
        off = offsets[instr[1]]
        genInstr('push -%d(%%ebp)' % (off))
        genInstr('push $outFormatInt')
        genInstr('call printf')
        genInstr('addl $8, %esp')

    elif instr[0] == 'scan':
        off = offsets[instr[1]]
        genInstr('lea -%d(%%ebp), %%eax' % (off))
        genInstr('push %eax')
        genInstr('push $inFormat')
        genInstr('call scanf')
        genInstr('addl $8, %esp')

    elif instr[0] == 'goto':
        genInstr('jmp %s' % (instr[1]))
    
    elif instr[0] == 'ifgoto':
        off = offsets[instr[1]]
        genInstr('movl -%d(%%ebp), %%eax' % (off))
        genInstr('cmp $0, %eax')
        genInstr('je %s' % (instr[2]))

    elif instr[0] == 'deref':
        off1= offsets[instr[1]]
        off2= offsets[instr[2]]
        genInstr('movl -%d(%%ebp), %%eax' % (off2))
        genInstr('movl (%%eax), %%ebx')
        genInstr('movl %%ebx, -%d(%%ebp)'%(off1))
closeFile()