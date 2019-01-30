import ply.lex as lex
import argparse

tokens = ('INT', 'OCT', 'HEX', 'FLOAT', 'STR', 'IMAGINARY', 'RUNE', 'BREAK', 'CASE', 'CHAN', 'CONST', 'CONTINUE', 'DEFAULT', 'DEFER', 'ELSE', 'FALLTHROUGH', 'FOR', 'FUNC', 'GO', 'GOTO', 'IF',
          'IMPORT', 'INTERFACE', 'MAP', 'PACKAGE', 'RANGE', 'RETURN', 'SELECT', 'STRUCT', 'SWITCH', 'TYPE', 'VAR', 'ADD', 'SUB', 'MULT', 'DIV',
          'MOD', 'ASSIGN', 'INC', 'DEC', 'EQ', 'NEQ', 'GT', 'LT', 'LEQ', 'GEQ', 'LOG_AND', 'LOG_OR', 'LOG_XOR', 'BIT_AND', 'BIT_OR', 'LSHIFT',
          'RSHIFT', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'AND_ASSIGN',
          'XOR_ASSIGN', 'OR_ASSIGN', 'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES',
          'COMMA', 'DOT', 'SEMI_COLON', 'COLON', 'IDENTIFIER', 'COMMENT')


keywords = {'BREAK', 'CASE', 'CHAN', 'CONST', 'CONTINUE', 'DEFAULT', 'DEFER', 'ELSE',
            'FALLTHROUGH', 'FOR', 'FUNC', 'GO', 'GOTO', 'IF', 'IMPORT', 'INTERFACE', 'MAP', 'PACKAGE', 'RANGE', 'RETURN', 'SELECT', 'STRUCT', 'SWITCH', 'TYPE', 'VAR'}

operators = {'ADD', 'SUB', 'MULT', 'DIV', 'MOD', 'ASSIGN', 'INC', 'DEC', 'EQ', 'NEQ', 'GT', 'LT', 'LEQ', 'GEQ', 'LOG_AND', 'LOG_OR', 'LOG_XOR', 'BIT_AND', 'BIT_OR', 'LSHIFT',
             'RSHIFT', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'AND_ASSIGN',
             'XOR_ASSIGN', 'OR_ASSIGN'}

separators = {'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES',
              'COMMA', 'DOT', 'SEMI_COLON', 'COLON'}

separators = {'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES',
              'COMMA', 'DOT', 'SEMI_COLON', 'COLON'}

reserved_keywords = {}

for r in keywords:
    reserved_keywords[r.lower()] = r


t_ignore = ' \t'
t_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
t_INC = r'\+\+'
t_DEC = r'--'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LEQ = r'<='
t_GEQ = r'>='
t_LOG_AND = r'&&'
t_LOG_OR = r'\|\|'
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULT_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_LSHIFT_ASSIGN = r'<<='
t_RSHIFT_ASSIGN = r'>>='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'\^='
t_OR_ASSIGN = r'\|='
t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_ASSIGN = r'='
t_LOG_XOR = r'\^'
t_BIT_OR = r'\|'
t_BIT_AND = r'&'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LEFT_PARANTHESIS = r'\)'
t_RIGHT_PARANTHESIS = r'\('
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACES = r'\{'
t_RIGHT_BRACES = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_SEMI_COLON = r';'
t_COLON = r':'

dec_lit = "(0|([1-9][0-9]*))"
oct_lit = "(0[0-7]*)"
hex_lit = "(0x|0X)[0-9a-fA-F]+"
float_lit = "[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?"
str_lit = """("[^"]*")|(`[^`]*`)"""
img_lit = "(" + dec_lit + "|" + float_lit + ")i"
rune_lit = "\'(.|(\\[abfnrtv]))\'"
identifier_lit = "[_a-zA-Z]+[a-zA-Z0-9_]*"


# def t_COMMENT(t):
#     r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
#     return t

# ill_pos=[]
@lex.TOKEN(str_lit)
def t_STR(t):
    # t.value = t.value[1:-1]
    return t

@lex.TOKEN(hex_lit)
def t_HEX(t):
    # t.value = int(t.value, 16)
    return t


@lex.TOKEN(float_lit)
def t_FLOAT(t):
    # t.value = float(t.value)
    return t


@lex.TOKEN(oct_lit)
def t_OCT(t):
    # t.value = int(t.value, 8)
    return t


@lex.TOKEN(dec_lit)
def t_INT(t):
    # t.value = int(t.value)
    return t


@lex.TOKEN(img_lit)
def t_IMAGINARY(t):
    # t.value = complex(t.value.replace('i', 'j'))
    return t


@lex.TOKEN(rune_lit)
def t_RUNE(t):
    # t.value = ord(t.value[1:-1])
    return t


@lex.TOKEN(identifier_lit)
def t_IDENTIFIER(t):
    t.type = reserved_keywords.get(t.value, 'IDENTIFIER')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal Token")
    # print(t.lexpos)
    # ill_pos.append(t)
    t.lexer.skip(1)


lexer = lex.lex()


parser = argparse.ArgumentParser()
parser.add_argument("--config", default="config.txt")
parser.add_argument("--input", default="data.txt")
parser.add_argument("--output", default="out.html")
args = parser.parse_args()


file = open(args.config, 'r')
colors = list(file)
file.close()

colour = {}

for j in range(len(colors)):
    key = ""
    c = ""
    f = 0
    color = colors[j]
    for i in range(len(color)):
        if(color[i] == ','):
            f = 1
            continue
        if(f):
            c += color[i]
        else:
            key += color[i]
    colour[key] = c.strip()


def find_color(tok):
    # print(tok)
    for op in operators:
        if(tok.type == op):
            return colour['operators']
    for key in keywords:
        if(tok.type == key):
            return colour['keywords']
    for sep in separators:
        if(tok.type == sep):
            return colour['separators']
    if(tok.type == 'STR'):
        return colour['string_literal']
    if(tok.type == 'HEX'):
        return colour['hex_literal']
    if(tok.type == 'OCT'):
        return colour['oct_literal']
    if(tok.type == 'INT'):
        return colour['dec_literal']
    if(tok.type == 'FLOAT'):
        return colour['float_literal']
    if(tok.type == 'COMMENT'):
        return colour['comments']
    if(tok.type == 'IDENTIFIER'):
        return colour['identifier']
    return 'black'


f = open(args.input, 'r')
lines = list(f)

outF = open(args.output, "w")
outF.write("<!DOCTYPE html>\n")
outF.write("<html>\n")
outF.write("<head><style>* {font-family: 'Consolas'}</style></head>")
outF.write("<body>\n")


fi=open(args.input,'r')
s=fi.read()
linestarts = [0]
for i in range(len(s)):
    if(s[i]=='\n'):
        linestarts = linestarts + [i+1]

lexer.input(s)
a = []
while(True):
    tok = lexer.token()
    if not tok:
        break
    a.append(tok)
cont = 0
line_count = 0
pos = 0

while(pos < len(s)):
    if(cont < len(a) and pos == a[cont].lexpos):
        dum = "<span style=\"color: %s\">" % find_color(a[cont])
        outF.write(dum)
        for i in range(pos, pos + len(a[cont].value)):
            writ = ''
            if s[i] == '\n':
                writ = '<br>\n'
            elif s[i] == ' ':
                writ = '&nbsp;'
            elif s[i] == '\t':
                writ = '&nbsp;&nbsp;&nbsp;&nbsp;'
            else:
                writ = s[i]
            pos += 1
            outF.write(writ)
        outF.write('</span>')
        cont += 1
    else:
        writ = ''
        if s[pos] == '\n':
            writ = '<br>\n'
        elif s[pos] == ' ':
            writ = '&nbsp;'
        elif s[pos] == '\t':
            writ = '&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            writ = s[pos]
        outF.write(writ)
        pos += 1
        


# for line in lines:
#     lexer.input(line)
#     a = []
#     while(True):
#         tok = lexer.token()
#         if not tok:
#             break
#         a.append(tok)
#     cont = 0
#     s = ""
#     i = 0
#     indentation = get_indentation_width(line)
#     outF.write('&nbsp' * indentation)
#     while(i < len(line)):
#         if(cont < len(a) and i == a[cont].lexpos):
#             dum = "<span style=\"color: %s\">" % find_color(a[cont])
#             outF.write(dum)
#             while(i < a[cont].lexpos+len(a[cont].value)):
#                 outF.write(line[i])
#                 i += 1
#             outF.write("</span>")
#             cont += 1
#         else:
#             outF.write(line[i])
#             i += 1
#     outF.write('<br/>')

outF.write("</body>\n")
outF.write("</html>\n")
outF.close()
