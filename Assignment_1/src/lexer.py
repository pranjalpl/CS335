import ply.lex as lex
import argparse

tokens = ('INT', 'OCT', 'HEX', 'FLOAT', 'STR', 'IMAGINARY', 'RUNE', 'BREAK', 'CASE', 'CHAN', 'CONST', 'CONTINUE', 'DEFAULT', 'DEFER', 'ELSE', 'FALLTHROUGH', 'FOR', 'FUNC', 'GO', 'GOTO', 'IF',
          'IMPORT', 'INTERFACE', 'MAP', 'PACKAGE', 'RANGE', 'RETURN', 'SELECT', 'STRUCT', 'SWITCH', 'TYPE', 'VAR', 'ADD', 'SUB', 'MULT', 'DIV',
          'MOD', 'ASSIGN', 'INC', 'DEC', 'EQ', 'NEQ', 'GT', 'LT', 'LEQ', 'GEQ', 'LOG_AND', 'LOG_OR', 'LOG_XOR', 'BIT_AND', 'BIT_OR', 'LSHIFT',
          'RSHIFT', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'AND_ASSIGN',
          'XOR_ASSIGN', 'OR_ASSIGN', 'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES',
          'COMMA', 'DOT', 'SEMI_COLON', 'COLON', 'IDENTIFIER')


keywords = {'BREAK', 'CASE', 'CHAN', 'CONST', 'CONTINUE', 'DEFAULT', 'DEFER', 'ELSE',
            'FALLTHROUGH', 'FOR', 'FUNC', 'GO', 'GOTO', 'IF', 'IMPORT', 'INTERFACE', 'MAP', 'PACKAGE', 'RANGE', 'RETURN', 'SELECT', 'STRUCT', 'SWITCH', 'TYPE', 'VAR'}

operators = {'ADD', 'SUB', 'MULT', 'DIV', 'MOD', 'ASSIGN', 'INC', 'DEC', 'EQ', 'NEQ', 'GT', 'LT', 'LEQ', 'GEQ', 'LOG_AND', 'LOG_OR', 'LOG_XOR', 'BIT_AND', 'BIT_OR', 'LSHIFT',
             'RSHIFT', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'AND_ASSIGN',
             'XOR_ASSIGN', 'OR_ASSIGN'}

separators = {'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES',
              'COMMA', 'DOT', 'SEMI_COLON', 'COLON'}

reserved_keywords = {}

for r in keywords:
    reserved_keywords[r.lower()] = r

t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
t_ignore = ' \t'
# t_ADD=r'\+'
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
str_lit = """("[^"]*")"""
img_lit = "(" + dec_lit + "|" + float_lit + ")i"
rune_lit = "\'(.|(\\[abfnrtv]))\'"
identifier_lit = "[_a-zA-Z]+[a-zA-Z0-9_]*"


@lex.TOKEN(dec_lit)
def t_INT(t):
    # t.value = int(t.value)
    return t


@lex.TOKEN(oct_lit)
def t_OCT(t):
    # t.value = int(t.value, 8)
    return t


@lex.TOKEN(hex_lit)
def t_HEX(t):
    # t.value = int(t.value, 16)
    return t


@lex.TOKEN(float_lit)
def t_FLOAT(t):
    # t.value = float(t.value)
    return t


@lex.TOKEN(str_lit)
def t_STR(t):
    # t.value = t.value[1:-1]
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
    print("Illegal Character")
    t.lexer.skip(1)


lexer = lex.lex()


parser = argparse.ArgumentParser()
parser.add_argument("--config", default="config.txt")
parser.add_argument("--input", default="data.txt")
parser.add_argument("--output", default="out.html")
args = parser.parse_args()

print(args.config)


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
    for op in operators:
        if(tok.type == op):
            return colour['operators']
    for key in keywords:
        if(tok.type == key):
            return colour['keywords']
    for sep in separators:
        if(tok.type == sep):
            return colour['separators']
    return 'black'


f = open(args.input, 'r')
lines = list(f)

outF = open(args.output, "w")
outF.write("<!DOCTYPE html>\n")
outF.write("<html>\n")
outF.write("<body>\n")

def get_indentation_width(line):
    i = 0
    ind = 0
    while line[i]==' ' or line[i]=='\t':
        i = i + 1
        if line[i]==' ':
            ind = ind + 1
        else:
            ind = ind + 4
    return ind

for line in lines:
    lexer.input(line)
    a = []
    while(True):
        tok = lexer.token()
        if not tok:
            break
        a.append(tok)
    cont = 0
    s = ""
    i = 0
    indentation = get_indentation_width(line)
    outF.write('&nbsp' * indentation)
    while(i < len(line)):
        if(cont < len(a) and i == a[cont].lexpos):
            dum = "<span style=\"color: %s\">" % find_color(a[cont])
            outF.write(dum)
            while(i < a[cont].lexpos+len(a[cont].value)):
                outF.write(line[i])
                i += 1
            outF.write("</span>")
            cont += 1
        else:
            outF.write(line[i])
            i += 1
    outF.write('<br/>')

outF.write("</body>\n")
outF.write("</html>\n")
outF.close()
