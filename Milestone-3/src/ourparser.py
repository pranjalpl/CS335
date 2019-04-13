import ply.yacc as yacc
import sys
import os
from lexer import *
from valid_assignments import *
from pprint import pprint
import inspect
import json
from utils import *
from symbol_table import *

# ----------------- SYMBOL TABLE HELPER FUNCTIONS -----------------------
scopeDict = {}
scopeDict[0] = symbolTable()
scopeStack = [0]
currentScope = 0
scopeSeq = 0
varCount = 0
firstFunc = True
labelCount = 1
labelDict = {}
rootNode = None
IR = []


def isUsed(name, scope):
    # code labels are also globals
    if (scope in ["globals", "labels"]):
        return scopeDict[0].getInfo(name) is not None

    # current scope
    if (scope == "."):
        return scopeDict[currentScope].getInfo(name) is not None

    # current scope excluding structures
    if (scope == ".!struct"):
        info = scopeDict[currentScope].getInfo(name)
        return info is not None and info['type'] != ('type' + name)

    # nearest variable from the current stack
    for s in scopeStack[::-1]:
        info = scopeDict[s].getInfo(name)
        if (info is not None) and (scope == "all" or scope == info['type']):
            return True
    return False
    # raise NameError("Flow should not reach here")


def add_scope(name=None):
    global scopeSeq
    global currentScope
    scopeSeq += 1
    lastScope = currentScope
    currentScope = scopeSeq
    scopeStack.append(currentScope)
    scopeDict[currentScope] = symbolTable()
    scopeDict[currentScope].setParent(lastScope)
    if name is not None:
        if type(name) is list:
            scopeDict[lastScope].insert(name[1], 'func')
            scopeDict[lastScope].updateArgList(
                name[1], 'child', scopeDict[currentScope])
        else:
            if isUsed(name, "."):
                raise NameError("Name " + name + " already defined")
            temp = currentScope
            currentScope = lastScope
            currentScope = temp
            scopeDict[lastScope].insert(name, 'type'+name)
            scopeDict[lastScope].updateArgList(
                name, 'child', scopeDict[currentScope])


def delete_scope():
    global currentScope
    currentScope = scopeStack.pop()
    currentScope = scopeStack[-1]


def new_temp():
    global varCount
    varCount += 1
    return 'var' + str(varCount - 1)


def new_label():
    global labelCount
    labelCount += 1
    return 'label' + str(labelCount - 1)


def find_info(name, scope=-1):
    if scope >= 0:
        info = scopeDict[scope].getInfo(name)
        if info is not None:
            return info
    else:
        for scope in scopeStack[::-1]:
            if scopeDict[scope].getInfo(name) is not None:
                info = scopeDict[scope].getInfo(name)
                return info
    raise NameError("Identifier " + name + " is not defined!")


def find_scope(name):
    # Nearest parent scope that has this identifier
    for scope in scopeStack[::-1]:
        if scopeDict[scope].getInfo(name) is not None:
            return scope
    raise NameError("Identifier " + name + " is not defined!")


def find_label(name):
    for scope in scopeStack[::-1]:
        if name in scopeDict[scope].extra:
            return scopeDict[scope].extra[name]
    raise ValueError("Not in any loop scope")

# -----------------------------------------------------------------------

# -------------- OTHER HELPER FUNCTIONS -----------
def findBinaryOp(arr):
    while type(arr[1]).__name__ != 'str':
        arr = arr[1]    
    return arr[1]
# -------------------------------------------------

# ------------- IR GENERATION -----------


class IRNode:
    idList = []
    code = []
    typeList = []
    placelist = []
    extra = {}
    def __init__(self):
        self.idList = []
        self.code = []
        self.typeList = []
        self.placelist = []
        self.extra = {}
    def __repr__(self):
        return '\n\tidList: ' + str(self.idList) + '\n\ttypeList: ' + str(self.typeList) + \
            '\n\tplacelist: ' + str(self.placelist) + '\n\textra: ' + str(self.extra) + '\n'
# ----------------------------------------


# ------------ PARSER ------------------
precedence = (
    ('right', 'ASSIGN', 'NOT'),
    ('left', 'LOG_OR'),
    ('left', 'LOG_AND'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'LT', 'GT', 'LEQ', 'GEQ'),
    ('left', 'LSHIFT', 'RSHIFT'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV', 'MOD'),
)

# ------------------------START----------------------------


def p_start(p):
    '''start : SourceFile'''
    # print(inspect.stack()[0][3])
    global rootNode
    p[0] = p[1]
    rootNode = p[0]
# -------------------------------------------------------


# -----------------------TYPES---------------------------
def p_type(p):
    '''Type : TypeName
            | TypeLit
            | LEFT_PARANTHESIS Type RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]
    print('\t\ttypes: ' + str(p[0].typeList))


def p_type_name(p):
    '''TypeName : TypeToken
                | QualifiedIdent'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    print('\t\ttypes: ' + str(p[0].typeList))


def p_type_token(p):
    '''TypeToken : INT_T
                 | FLOAT_T
                 | UINT_T
                 | COMPLEX_T
                 | RUNE_T
                 | BOOL_T
                 | STRING_T
                 | TYPE IDENTIFIER'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    if len(p) == 3:
        if not isUsed(p[2], 'all'):
            raise TypeError("Typename " + p[2] + " not defined")
        else:
            p[0].typeList.append(find_info(p[2], 0)['type'])
    else:
        p[0].typeList.append(p[1])


def p_type_lit(p):
    '''TypeLit : ArrayType
               | StructType
               | PointerType'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_type_opt(p):
    '''TypeOpt : Type
               | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# -------------------------------------------------------


# ------------------- ARRAY TYPE -------------------------
def p_array_type(p):
    '''ArrayType : LEFT_BRACKET ArrayLength RIGHT_BRACKET ElementType'''
    # print(inspect.stack()[0][3])
    p[0] = ["ArrayType", "[", p[2], "]", p[4]]
    p[0] = IRNode()
    # p[0].code = p[2].code
    p[0].typeList.append("*" + p[4].typeList[0])
    p[0].extra['sizeOfArray'] = int(p[2])
    scopeDict[currentScope].currOffset += 4*int(p[2])

# TODO: Modify this to accept only integers
def p_array_length(p):
    '''ArrayLength :  I INTEGER
                    | I OCTAL
                    | I HEX
                    | I RUNE'''
    # print(inspect.stack()[0][3])
    p[0] = int(p[2])

def p_element_type(p):
    ''' ElementType : Type '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# --------------------------------------------------------


# ----------------- STRUCT TYPE ---------------------------
def p_struct_type(p):
    '''StructType : CreateFuncScope STRUCT LEFT_BRACES FieldDeclRep RIGHT_BRACES EndScope'''
    # print(inspect.stack()[0][3])
    p[0] = p[4]
    p[0].typeList = [find_info(p[-1], 0)]


def p_field_decl_rep(p):
    ''' FieldDeclRep : FieldDeclRep FieldDecl SEMICOLON
                    | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) < 4:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].idList += p[2].idList
        p[0].typeList += p[2].typeList


def p_field_decl(p):
    ''' FieldDecl : IdentifierList Type'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    for i in range(0, len(p[0].idList)):
        scopeDict[currentScope].updateArgList(p[0].idList[i], 'type', p[2].typeList[0])
        scopeDict[currentScope].updateArgList(p[0].placelist[i], 'type', p[2].typeList[0])
        if 'sizeOfArray' in dict.keys(p[2].extra):
            scopeDict[currentScope].updateArgList(p[1].idList[i], 'size', p[2].extra['sizeOfArray'])
            scopeDict[currentScope].updateArgList(p[1].placelist[i], 'size', p[2].extra['sizeOfArray'])


def p_TagOpt(p):
    ''' TagOpt : Tag
                | epsilon '''
    # print(inspect.stack()[0][3])
    p[0] = ["TagOpt", p[1]]


def p_Tag(p):
    ''' Tag : STRING '''
    # print(inspect.stack()[0][3])
    p[0] = ["Tag", p[1]]
# ---------------------------------------------------------


# ------------------POINTER TYPES--------------------------
def p_point_type(p):
    '''PointerType : MULT BaseType'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]
    p[0].typeList[0] = "*" + p[0].typeList[0]


def p_base_type(p):
    '''BaseType : Type'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# ---------------------------------------------------------


# ---------------FUNCTION TYPES----------------------------
def p_sign(p):
    '''Signature : Parameters TypeOpt'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    p[0].paramTypeList = p[1].typeList
    scopeDict[0].insert(p[-2][1], 'signatureType')
    if len(p[2].typeList) == 0:
        scopeDict[0].updateArgList(p[-2][1], 'retType', 'void')
    else:
        scopeDict[0].updateArgList(p[-2][1], 'retType', p[2].typeList[0])

    info = find_info(p[-2][1], 0)
    if 'label' not in info:
        labeln = new_label()
        scopeDict[0].updateArgList(p[-2][1], 'label', labeln)
        scopeDict[0].updateArgList(p[-2][1], 'child', scopeDict[currentScope])
        info['paramsTypeList'] = p[1].typeList

# XXX


def p_result_opt(p):
    '''ResultOpt : Result
                 | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = ["ResultOpt", p[1]]

# XXX


def p_result(p):
    '''Result : Parameters
              | Type'''
    # print(inspect.stack()[0][3])
    p[0] = ["Result", p[1]]


def p_params(p):
    '''Parameters : LEFT_PARANTHESIS ParameterListOpt RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]


def p_param_list_opt(p):
    '''ParameterListOpt : ParametersList
                             | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_param_list(p):
    '''ParametersList : ParameterDecl
                      | ParameterDeclCommaRep'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_param_decl_comma_rep(p):
    '''ParameterDeclCommaRep : ParameterDeclCommaRep COMMA ParameterDecl
                             | ParameterDecl COMMA ParameterDecl'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    # XXX: Erroneous code? shouldnt it be p[1].typeList + p[3].typeList instead of p[3].typeList alone
    p[0].idList += p[3].idList
    p[0].typeList += p[3].typeList
    p[0].placelist += p[3].placelist


def p_param_decl(p):
    # '''ParameterDecl : IdentifierList Type'''
    '''ParameterDecl : IdentifierList Type
                     | Type'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    if len(p) == 3:
        for i in range(len(p[1].idList)):
            scopeDict[currentScope].updateArgList(p[1].idList[i], 'type', p[2].typeList[0])
            scopeDict[currentScope].updateArgList(p[1].placelist[i], 'type', p[2].typeList[0])
            if 'sizeOfArray' in dict.keys(p[2].extra):
                scopeDict[currentScope].updateArgList(p[1].idList[i], 'size', p[2].extra['sizeOfArray'])
                scopeDict[currentScope].updateArgList(p[1].placelist[i], 'size', p[2].extra['sizeOfArray'])
                
            p[0].typeList.append(p[2].typeList[0])
    else:
        p[0].typeList = p[1].typeList
# ---------------------------------------------------------


# -----------------------BLOCKS---------------------------
def p_block(p):
    '''Block : LEFT_BRACES StatementList RIGHT_BRACES'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]


def p_stat_list(p):
    '''StatementList : StatementRep'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_stat_rep(p):
    '''StatementRep : StatementRep Statement SEMICOLON
                    | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[2].code
    else:
        p[0] = p[1]
# -------------------------------------------------------


# ------------------DECLARATIONS and SCOPE------------------------
def p_decl(p):
    '''Declaration : ConstDecl
                    | TypeDecl
                    | VarDecl'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_toplevel_decl(p):
    '''TopLevelDecl : Declaration
                    | FunctionDecl'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# -------------------------------------------------------


# ------------------CONSTANT DECLARATIONS----------------
def p_const_decl(p):
    '''ConstDecl : CONST ConstSpec
                 | CONST LEFT_PARANTHESIS ConstSpecRep RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[3]


def p_const_spec_rep(p):
    '''ConstSpecRep : ConstSpecRep ConstSpec SEMICOLON
                    | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[2].code
    else:
        p[0] = p[1]


def p_const_spec(p):
    '''ConstSpec : IdentifierList Type ASSIGN ExpressionList'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].code = p[1].code + p[4].code

    if(len(p[1].placelist) != len(p[4].placelist)):
        raise ValueError(
            "Error: unequal number of identifiers and expressions for assignment")

    for x in range(len(p[1].placelist)):
        if (p[4].typeList[x]).startswith('lit'):
            p[0].code.append(["=", p[1].placelist[x], p[4].placelist[x]])
        p[1].placelist[x] = p[4].placelist[x]
        scope = find_scope(p[1].idList[x])
        scopeDict[scope].updateArgList(
            p[1].idList[x], 'place', p[1].placelist[x])

        # type insertion
        scopeDict[scope].updateArgList(
            p[1].idList[x], 'type', p[2].typeList[0])
        scopeDict[scope].updateArgList(
            p[1].placelist[x], 'type', p[2].typeList[0])
        if 'sizeOfArray' in dict.keys(p[2].extra):
            scopeDict[currentScope].updateArgList(p[1].idList[i], 'size', p[2].extra['sizeOfArray'])
            scopeDict[currentScope].updateArgList(p[1].placelist[i], 'size', p[2].extra['sizeOfArray'])
    # TODO type checking
# XXX


def p_type_expr_list(p):
    '''TypeExprListOpt : TypeOpt ASSIGN ExpressionList
                       | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = ["TypeExprListOpt", p[1], "=", p[3]]
    else:
        p[0] = ["TypeExprListOpt", p[1]]


def p_identifier_list(p):
    '''IdentifierList : IDENTIFIER IdentifierRep'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]
    p[0].idList = [p[1]] + p[0].idList
    if isUsed(p[1], "."):
        raise NameError("Error: " + p[1] + " already exists")
    else:
        scopeDict[currentScope].insert(p[1], 'int_t')
        nameTemp = new_temp()
        p[0].placelist = [nameTemp] + p[0].placelist
        scopeDict[currentScope].updateArgList(p[1], 'place', nameTemp)
        scopeDict[currentScope].updateArgList(p[1], 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        scopeDict[currentScope].insert(nameTemp, 'int_t')
        scopeDict[currentScope].updateArgList(nameTemp, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4


def p_identifier_rep(p):
    '''IdentifierRep : IdentifierRep COMMA IDENTIFIER
                     | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        if isUsed(p[3], "."):
            raise NameError("ERROR: " + p[3] + " already exists")
        else:
            p[0] = p[1]
            scopeDict[currentScope].insert(p[3], 'int_t')
            nameTemp = new_temp()
            p[0].placelist = p[0].placelist + [nameTemp]
            scopeDict[currentScope].updateArgList(p[3], 'place', nameTemp)
            p[0].idList.append(p[3])
            scopeDict[currentScope].updateArgList(p[3], 'offset', scopeDict[currentScope].currOffset + 4)
            scopeDict[currentScope].currOffset += 4
            scopeDict[currentScope].insert(nameTemp, 'int_t')
            scopeDict[currentScope].updateArgList(nameTemp, 'offset', scopeDict[currentScope].currOffset + 4)
            scopeDict[currentScope].currOffset += 4
    else:
        p[0] = p[1]


def p_expr_list(p):
    '''ExpressionList : Expression ExpressionRep'''
    p[0] = p[2]
    p[0].code = p[1].code+p[0].code
    p[0].placelist = p[1].placelist + p[0].placelist
    print(p.lexer.lineno, 'qwer', p[1].typeList, p[0].typeList)
    p[0].typeList = p[1].typeList + p[0].typeList
    if 'AddrList' not in p[1].extra:
        p[1].extra['AddrList'] = ['None']
    p[0].extra['AddrList'] += p[1].extra['AddrList']


def p_expr_rep(p):
    '''ExpressionRep : ExpressionRep COMMA Expression
                     | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[3].code
        p[0].placelist += p[3].placelist
        p[0].typeList += p[3].typeList
        print('\t\ttypes: ' + str(p[0].typeList))
        if 'AddrList' not in p[3].extra:
            p[3].extra['AddrList'] = ['None']
        p[0].extra['AddrList'] += p[3].extra['AddrList']
    else:
        p[0] = p[1]
        p[0].extra['AddrList'] = []
# -------------------------------------------------------


# ------------------TYPE DECLARATIONS-------------------
def p_type_decl(p):
    '''TypeDecl : TYPE TypeSpec
                | TYPE LEFT_PARANTHESIS TypeSpecRep RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = p[2]


def p_type_spec_rep(p):
    '''TypeSpecRep : TypeSpecRep TypeSpec SEMICOLON
                   | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = IRNode()
    else:
        p[0] = p[1]


def p_type_spec(p):
    '''TypeSpec : TypeDef'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]

# XXX


def p_alias_decl(p):
    '''AliasDecl : IDENTIFIER ASSIGN Type'''
    # print(inspect.stack()[0][3])
    p[0] = ["AliasDecl", p[1], '=', p[3]]
# -------------------------------------------------------


# -------------------TYPE DEFINITIONS--------------------
def p_type_def(p):
    '''TypeDef : IDENTIFIER Type'''
    # print(inspect.stack()[0][3])
    if isUsed(p[1], ".!struct"):
        raise NameError("ERROR: " + p[1] + " already exists, can't redefine")
    else:
        scopeDict[currentScope].insert(p[1], p[2].typeList[0])
    p[0] = IRNode()
# -------------------------------------------------------


# ----------------VARIABLE DECLARATIONS------------------
def p_var_decl(p):
    '''VarDecl : VAR VarSpec
               | VAR LEFT_PARANTHESIS VarSpecRep RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[3]


def p_var_spec_rep(p):
    '''VarSpecRep : VarSpecRep VarSpec SEMICOLON
                  | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[2].code
    else:
        p[0] = p[1]


def p_var_spec(p):
    '''VarSpec : IdentifierList Type ExpressionListOpt
               | IdentifierList ASSIGN ExpressionList'''
    # print(inspect.stack()[0][3])
    if p[2] == '=':
        p[0] = IRNode()
        p[0].code = p[1].code + p[3].code

        if(len(p[1].placelist) != len(p[3].placelist)):
            raise ValueError(
                "Error: mismatch in number of identifiers and expressions for asisgnment")

        for x in range(len(p[1].placelist)):
            scope = find_scope(p[1].idList[x])
            if (p[3].typeList[x]).startswith('lit'):
                p[0].code.append(["=", p[1].placelist[x], p[3].placelist[x]])
                scopeDict[scope].updateArgList(
                    p[1].idList[x], 'type', p[3].typeList[x][3:])
                scopeDict[scope].updateArgList(
                    p[1].placelist[x], 'type', p[3].typeList[x][3:])
            else:
                scopeDict[scope].updateArgList(
                    p[1].idList[x], 'type', p[3].typeList[x])
                scopeDict[scope].updateArgList(
                    p[1].placelist[x], 'type', p[3].typeList[x])
                if 'sizeOfArray' in dict.keys(p[3].extra):
                    scopeDict[currentScope].updateArgList(p[1].idList[i], 'size', p[3].extra['sizeOfArray'])
                    scopeDict[currentScope].updateArgList(p[1].placelist[i], 'size', p[3].extra['sizeOfArray'])

            p[1].placelist[x] = p[3].placelist[x]
            scopeDict[scope].updateArgList(
                p[1].idList[x], 'place', p[1].placelist[x])
    else:
        if len(p[3].placelist) == 0:
            p[0] = p[1]
            for x in range(len(p[1].idList)):
                scope = find_scope(p[1].idList[x])
                scopeDict[scope].updateArgList(
                    p[1].idList[x], 'type', p[2].typeList[0])
                scopeDict[scope].updateArgList(
                    p[1].placelist[x], 'type', p[2].typeList[0])
                if 'sizeOfArray' in dict.keys(p[2].extra):
                    scopeDict[scope].updateArgList(p[1].idList[x], 'size', p[2].extra['sizeOfArray'])
                    scopeDict[scope].updateArgList(p[1].placelist[x], 'size', p[2].extra['sizeOfArray'])
            return
        p[0] = IRNode()
        p[0].code = p[1].code + p[3].code
        if(len(p[1].placelist) != len(p[3].placelist)):
            raise ValueError(
                "Error: mismatch in number of identifiers and expressions for asisgnment")

        for x in range(len(p[1].placelist)):
            if not (p[3].typeList[x]).startswith('lit'):
                p[0].code.append(["=", p[1].placelist[x], p[3].placelist[x]])
            p[1].placelist[x] = p[3].placelist[x]

            scope = find_scope(p[1].idList[x])
            scopeDict[scope].updateArgList(
                p[1].idList[x], 'place', p[1].placelist[x])
            scopeDict[scope].updateArgList(
                p[1].idList[x], 'type', p[2].typeList[0])
            scopeDict[scope].updateArgList(
                p[1].placelist[x], 'type', p[2].typeList[0])
            if 'sizeOfArray' in dict.keys(p[2].extra):
                scopeDict[scope].updateArgList(p[1].idList[x], 'size', p[2]['sizeOfArray'])
                scopeDict[scope].updateArgList(p[1].placelist[x], 'size', p[2]['sizeOfArray'])

            # TODO typelist check required
            currType = p[2].typeList[0]
            for i in range(0, len(p[3].typeList)):
                comp = p[3].typeList[i]
                if comp.startswith('lit'):
                    comp = comp[3:]
                print('\tComparing types', currType, comp, isValidAssignment(currType, comp))
                if not isValidAssignment(currType, comp):
                    raise ValueError("Type of " + comp + " cannot be assigned to " + currType)
            print('Type Checking:', p[3], currType)

def p_expr_list_opt(p):
    '''ExpressionListOpt : ASSIGN ExpressionList
                         | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        print('\t\t' + str(p[2]))
        p[0] = p[2]
    else:
        p[0] = p[1]
# -------------------------------------------------------


# ----------------SHORT VARIABLE DECLARATIONS-------------
def p_short_var_decl(p):
    ''' ShortVarDecl : IDENTIFIER QUICK_ASSIGN Expression '''
    # print(inspect.stack()[0][3])
    if isUsed(p[1], "."):
        raise NameError("ERROR: " + p[1] + " already exists")
    else:
        scopeDict[currentScope].insert(p[1], None)
    p[0] = IRNode()
    newVar = new_temp()
    scopeDict[currentScope].insert(newVar, 'int_t')
    scopeDict[currentScope].updateArgList(newVar, 'offset', scopeDict[currentScope].currOffset + 4)
    scopeDict[currentScope].currOffset += 4
    p[0].code = p[3].code
    p[0].code.append(['=', newVar, p[3].placelist[0]])
    scopeDict[currentScope].updateArgList(p[1], 'place', newVar)
    scopeDict[currentScope].updateArgList(p[1], 'type', p[3].typeList[0])
# -------------------------------------------------------


# ----------------FUNCTION DECLARATIONS------------------
def p_func_decl(p):
    '''FunctionDecl : FUNC FunctionName CreateScope Function EndScope
                    | FUNC FunctionName CreateScope Signature EndScope'''
    # print(inspect.stack()[0][3])
    if not len(p[4].code):
        p[0] = IRNode()
        return

    p[0] = IRNode()
    global firstFunc
    if firstFunc:
        firstFunc = False
        p[0].code = [["goto", "label0"]]
    info = find_info(p[2][1])
    # print('hehe', info)
    # info['paramTypeList'] = 
    label = info['label']
    p[0].code.append([label + ':'])
    p[0].code += p[4].code


def p_create_func_scope(p):
    '''CreateFuncScope : '''
    # print(inspect.stack()[0][3])
    add_scope(p[-1])


def p_create_scope(p):
    '''CreateScope : '''
    # print(inspect.stack()[0][3])
    add_scope()


def p_delete_scope(p):
    '''EndScope : '''
    # print(inspect.stack()[0][3])
    delete_scope()


def p_func_name(p):
    '''FunctionName : IDENTIFIER'''
    # print(inspect.stack()[0][3])
    p[0] = ["FunctionName", p[1]]


def p_func(p):
    '''Function : Signature FunctionBody'''
    # print(inspect.stack()[0][3])
    # DONE typechecking of return type. It should be same as defined in signature
    p[0] = p[2]
    for x in range(len(p[1].idList)):
        info = find_info(p[1].idList[x])
        p[0].code = [['pop', len(p[1].idList) - x - 1,
                      info['place']]] + p[0].code

    if isUsed(p[-2][1], "signatureType"):
        if p[-2][1] == "main":
            scopeDict[0].updateArgList("main", "label", "label0")
            scopeDict[0].updateArgList(
                "main", 'child', scopeDict[currentScope])

        info = find_info(p[-2][1])
        info['type'] = 'func'
        print('inside function->signature body', p.lexer.lineno, p[-1])
    else:
        print(scopeDict)
        print(scopeStack)
        raise NameError('no signature for ' + p[-2][1] + '!')


def p_func_body(p):
    '''FunctionBody : Block'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# -------------------------------------------------------


# ----------------------OPERAND----------------------------
def p_operand(p):
    '''Operand : Literal
               | OperandName
               | LEFT_PARANTHESIS Expression RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_literal(p):
    '''Literal : BasicLit'''
    # print(inspect.stack()[0][3])
    # | CompositeLit'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_basic_lit(p):
    '''BasicLit : I INTEGER
                | I OCTAL
                | I HEX
                | F FLOAT
                | C IMAGINARY
                | I RUNE
                | S STRING'''
    # print(inspect.stack()[0][3])
    p[0] = ["BasicLit", str(p[1])]
    p[0] = IRNode()
    name = new_temp()
    p[0].code.append(["=", name, p[2]])
    p[0].placelist.append(name)
    p[0].typeList.append('lit' + p[1])
    
    scopeDict[currentScope].insert(name, p[1])
    scopeDict[currentScope].updateArgList(name, 'place', name)
    scopeDict[currentScope].updateArgList(name, 'type', p[1])
    scopeDict[currentScope].updateArgList(name, 'offset', scopeDict[currentScope].currOffset + 4)
    scopeDict[currentScope].currOffset += 4

    print('\t\ttypes: ' + str(p[0].typeList))


def p_I(p):
    ''' I : '''
    # print(inspect.stack()[0][3])
    p[0] = 'int_t'


def p_F(p):
    ''' F : '''
    # print(inspect.stack()[0][3])
    p[0] = 'float_t'


def p_C(p):
    ''' C : '''
    # print(inspect.stack()[0][3])
    p[0] = 'complex_t'


def p_S(p):
    ''' S : '''
    # print(inspect.stack()[0][3])
    p[0] = 'string_t'


def p_operand_name(p):
    '''OperandName : IDENTIFIER'''
    # print(inspect.stack()[0][3])
    if not isUsed(p[1], "all"):
        raise NameError("ERROR: " + p[1] + " not defined")
    p[0] = IRNode()
    info = find_info(p[1])
    if info['type'] == 'func' or info['type'] == 'signatureType':
        p[0].typeList = [info['retType']]
        # # TODO type check here
        # for i in range(len(p[0].typeList)):
        #     if p[0].typeList[i] != 1:

        p[0].placelist.append(info['label'])
    else:
        p[0].typeList = [info['type']]
        p[0].placelist.append(info['place'])
    p[0].idList = [p[1]]
# ---------------------------------------------------------


# -------------------QUALIFIED IDENTIFIER----------------
def p_quali_ident(p):
    '''QualifiedIdent : IDENTIFIER DOT TypeName'''
    # print(inspect.stack()[0][3])
    if not isUsed(p[1], "package"):
        raise NameError("Package " + p[1] + " not included")
    p[0] = IRNode()
    p[0].typeList.append(p[1] + p[2] + p[3].typeList[0])
    
    # '''QualifiedIdent : IDENTIFIER DOT TypeName'''
    print(inspect.stack()[0][3])
    # typ = scopeDict[0].getInfo(p[1][4:])
    # a = p[1].idList[0].startswith('type')
    # b = isUsed(p[1], "package")
    # if not a and not b:
    #     raise NameError("Package " + p[1] + " not included")
    # if a:
    #     c = typ['child']['table'].keys()
    #     if not p[1] in c:
    #         raise TypeError('%s does not contain the member %s'%())
# -------------------------------------------------------

# ------------------PRIMARY EXPRESSIONS--------------------


def p_prim_expr(p):
    '''PrimaryExpr : Operand
                   | PrimaryExpr Selector
                   | Conversion
                   | PrimaryExpr LEFT_BRACKET Expression RIGHT_BRACKET
                   | PrimaryExpr Slice
                   | PrimaryExpr TypeAssertion
                   | PrimaryExpr LEFT_PARANTHESIS ExpressionListTypeOpt RIGHT_PARANTHESIS'''
    print(inspect.stack()[0][3], p)
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '[':
        p[0] = p[1]
        p[0].code += p[3].code

        newPlace4 = new_temp()
        p[0].code.append(['=', newPlace4, '4'])

        newPlace3 = new_temp()
        p[0].code.append(['x', newPlace3, p[3].placelist[0], newPlace4])

        newPlace = new_temp()
        p[0].code.append(['+', newPlace, p[0].placelist[0], newPlace3])

        newPlace2 = new_temp()
        p[0].code.append(['*', newPlace2, newPlace])

    
        scopeDict[currentScope].insert(p[0], 'int_t')
        scopeDict[currentScope].updateArgList(newPlace4, 'place', newPlace4)
        scopeDict[currentScope].updateArgList(newPlace4, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
    
        scopeDict[currentScope].insert(p[0], 'int_t')
        scopeDict[currentScope].updateArgList(newPlace3, 'place', newPlace3)
        scopeDict[currentScope].updateArgList(newPlace3, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4

        scopeDict[currentScope].insert(p[0], 'int_t')
        scopeDict[currentScope].updateArgList(newPlace, 'place', newPlace)
        scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
    
        scopeDict[currentScope].insert(p[0], 'int_t')
        scopeDict[currentScope].updateArgList(newPlace2, 'place', newPlace2)
        scopeDict[currentScope].updateArgList(newPlace2, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4

        p[0].extra['AddrList'] = [newPlace]
        p[0].placelist = [newPlace2]
        p[0].typeList = [p[1].typeList[0][1:]]

    elif p[2] == '(':
        p[0] = p[1]
        p[0].code.append(['save_registers'])
        p[0].code += p[3].code
        if len(p[3].placelist):
            for x in p[3].placelist:
                p[0].code.append(['push', x])

        info = find_info(p[1].idList[0], 0)
        print(info, p.lexer.lineno, p[-1])
        paramsTypes = info['paramsTypeList']
        # TODO: Overload here
        if len(paramsTypes) != len(p[3].typeList):
            print(paramsTypes, p[3].typeList, p.lexer.lineno, 'asdf')
            raise Exception('Argument number mismatch: %d v/s %d Line: %d'%(len(paramsTypes), len(p[3].typeList), p.lexer.lineno))
        for i in range(len(paramsTypes)):
            if not isValidAssignment(paramsTypes[i], p[3].typeList[i]):
                raise Exception('Incompatible argument types %s v/s %s:'%(paramsTypes[i], p[3].typeList[i]))

        if info['retType'] == 'void':
            p[0].code.append(['call', info['label']])
        else:
            newPlace = new_temp()
            p[0].placelist = [newPlace]
            p[0].code.append(['call', newPlace, info['label']])
            p[0].code.append(['restore_registers'])
            scopeDict[currentScope].insert(newPlace, 'int_t')
            scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
            scopeDict[currentScope].currOffset += 4
        # TODO type checking
        p[0].typeList = [p[1].typeList[0]]
    else:
        if not len(p[2].placelist):
            p[0] = IRNode()
        else:
            p[0] = p[1]
            p[0].placelist = p[2].placelist
            p[0].typeList = p[2].typeList


def p_selector(p):
    '''Selector : DOT IDENTIFIER'''
    p[0] = IRNode()
    info = find_info(p[-1].idList[0])
    structName = info['type'][4:]
    infoStruct = find_info(structName, 0)
    newScopeTable = infoStruct['child']
    if p[2] not in newScopeTable.table:
        raise NameError("struct " + structName + " has no member " + p[2])

    s = p[-1].idList[0] + "." + p[2]
    if isUsed(s, 'current'):
        info = find_info(s)
        p[0].placelist = [info['place']]
        p[0].typeList = [info['type']]
    else:
        newPlace = new_temp()
        p[0].placelist = [newPlace]
        scopeDict[currentScope].insert(newPlace, 'int_t')
        scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        typedata = newScopeTable.getInfo(p[2])
        p[0].typeList = [typedata['type']]
        scopeDict[currentScope].insert(s, p[0].typeList[0])
        scopeDict[currentScope].updateArgList(s, 'place', p[0].placelist[0])


def p_index(p):
    '''Index : LEFT_BRACKET Expression RIGHT_BRACKET'''
    # print(inspect.stack()[0][3])
    p[0] = ["Index", "[", p[2], "]"]


def p_slice(p):
    '''Slice : LEFT_BRACKET ExpressionOpt COLON ExpressionOpt RIGHT_BRACKET
             | LEFT_BRACKET ExpressionOpt COLON Expression COLON Expression RIGHT_BRACKET'''
    # print(inspect.stack()[0][3])
    if len(p) == 6:
        p[0] = ["Slice", "[", p[2], ":", p[4], "]"]
    else:
        p[0] = ["Slice", "[", p[2], ":", p[4], ":", p[6], "]"]


def p_type_assert(p):
    '''TypeAssertion : DOT LEFT_PARANTHESIS Type RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    p[0] = ["TypeAssertion", ".", "(", p[3], ")"]


def p_expr_list_type_opt(p):
    '''ExpressionListTypeOpt : ExpressionList
                             | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
# ---------------------------------------------------------


# ----------------------OPERATORS-------------------------
def p_expr(p):
    '''Expression : UnaryExpr
                  | Expression BinaryOp Expression'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[3].code
        newPlace = new_temp()
        p[0].code.append([findBinaryOp(p[2]), newPlace, p[1].placelist[0], p[3].placelist[0]])
        p[0].placelist = [newPlace]
        scopeDict[currentScope].insert(newPlace, 'int_t')
        scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4

        left = p[1].typeList[0]
        if left.startswith('lit'):
            left = left[3:]
        right = p[3].typeList[0]
        if right.startswith('lit'):
            right = right[3:]
        op = findBinaryOp(p[2])
        isValid = isValidBinaryOp(op, left, right)
        if isValid == -1:
            raise ValueError(op + " is not applicable to types: " + left + " and " + right)
        else:
            p[0].typeList = [validBinaryOps[isValid]['returns']]
    else:
        p[0] = p[1]


def p_expr_opt(p):
    '''ExpressionOpt : Expression
                     | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_unary_expr(p):
    '''UnaryExpr : PrimaryExpr
                 | UnaryOp UnaryExpr
                 | NOT UnaryExpr'''
    # print(inspect.stack()[0][3])
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == "!":
        p[0] = p[2]
        newPlace = new_temp()
        scopeDict[currentScope].insert(newPlace, 'int_t')
        scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        p[0].code.append(["!", newPlace, p[2].placelist[0]])
        p[0].placelist = [newPlace]
    else:
        p[0] = p[2]
        newPlace = new_temp()
        scopeDict[currentScope].insert(newPlace, 'int_t')
        scopeDict[currentScope].updateArgList(newPlace, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        if p[1][1] == "-" or p[1][1] == '+':
            newPlace2 = new_temp()
            scopeDict[currentScope].insert(newPlace2, 'int_t')
            scopeDict[currentScope].updateArgList(newPlace2, 'offset', scopeDict[currentScope].currOffset + 4)
            scopeDict[currentScope].currOffset += 4
            p[0].append(['=', newPlace2, 0])
            p[0].append([p[1][1], newPlace, newPlace2, p[2].placelist[0]])
        elif p[1][1] == "&":
            p[0].code.append([p[1][1], newPlace, p[2].placelist[0]])
            p[0].typeList[0] = ('*' + p[0].typeList[0])
        else:
            p[0].code.append([p[1][1], newPlace, p[2].placelist[0]])
        p[0].placelist = [newPlace]


def p_binary_op(p):
    '''BinaryOp : LOG_OR
                | LOG_AND
                | RelOp
                | AddMulOp'''
    # print(inspect.stack()[0][3])
    if p[1] == "||":
        p[0] = ["BinaryOp", "||"]
    elif p[1] == "&&":
        p[0] = ["BinaryOp", "&&"]
    else:
        p[0] = ["BinaryOp", p[1]]

# XXX
def p_rel_op(p):
    '''RelOp : EQ
             | NEQ
             | LT
             | GT
             | LEQ
             | GEQ'''
    # print(inspect.stack()[0][3])
    if p[1] == "==":
        p[0] = ["RelOp", "=="]
    elif p[1] == "!=":
        p[0] = ["RelOp", "!="]
    elif p[1] == "<":
        p[0] = ["RelOp", "<"]
    elif p[1] == ">":
        p[0] = ["RelOp", ">"]
    elif p[1] == "<=":
        p[0] = ["RelOp", "<="]
    elif p[1] == ">=":
        p[0] = ["RelOp", ">="]

# XXX
def p_add_mul_op(p):
    '''AddMulOp : UnaryOp
                | OR
                | XOR
                | DIV
                | MOD
                | LSHIFT
                | RSHIFT'''
    # print(inspect.stack()[0][3])
    if p[1] == "/":
        p[0] = ["AddMulOp", "/"]
    elif p[1] == "%":
        p[0] = ["AddMulOp", "%"]
    elif p[1] == "|":
        p[0] = ["AddMulOp", "|"]
    elif p[1] == "^":
        p[0] = ["AddMulOp", "^"]
    elif p[1] == "<<":
        p[0] = ["AddMulOp", "<<"]
    elif p[1] == ">>":
        p[0] = ["AddMulOp", ">>"]
    else:
        p[0] = ["AddMulOp", p[1]]


def p_unary_op(p):
    '''UnaryOp : ADD
               | SUB
               | MULT
               | AND '''
    # print(inspect.stack()[0][3])
    if p[1] == '+':
        p[0] = ["UnaryOp", "+"]
    elif p[1] == '-':
        p[0] = ["UnaryOp", "-"]
    elif p[1] == '*':
        p[0] = ["UnaryOp", "*"]
    elif p[1] == '&':
        p[0] = ["UnaryOp", "&"]
# -------------------------------------------------------


# -----------------CONVERSIONS-----------------------------
def p_conversion(p):
    '''Conversion : TYPECAST Type LEFT_PARANTHESIS Expression RIGHT_PARANTHESIS'''
    # print(inspect.stack()[0][3])
    p[0] = p[4]
    p[0].typeList = [p[1].typeList[0]]
# ---------------------------------------------------------


# ---------------- STATEMENTS -----------------------
def p_statement(p):
    '''Statement : Declaration
                 | LabeledStmt
                 | SimpleStmt
                 | ReturnStmt
                 | CreateScope Block EndScope
                 | ScanStmt
                 | BreakStmt
                 | ContinueStmt
                 | GotoStmt
                 | PrintStmt
                 | IfStmt
                 | SwitchStmt
                 | ForStmt '''
    # print(inspect.stack()[0][3])
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_print_stmt(p):
    ''' PrintStmt : PRINT Expression '''
    # print(inspect.stack()[0][3])
    p[0] = p[2]
    p[0].code.append(['print', p[2].placelist[0]])


def p_scan_stmt(p):
    ''' ScanStmt : SCAN Expression '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].code.append(['scan', p[2].placelist[0]])


def p_simple_stmt(p):
    ''' SimpleStmt : epsilon
                    | ExpressionStmt
                    | IncDecStmt
                    | Assignment
                    | ShortVarDecl '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_labeled_statements(p):
    ''' LabeledStmt : Label COLON Statement '''
    # print(inspect.stack()[0][3])
    if isUsed(p[1][1], "label"):
        raise NameError("Label " + p[1][1] + " already exists")
    newl = ''
    if p[1][1] in labelDict:
        scopeDict[0].insert(p[1][1], "label")
        scopeDict[0].updateArgList(p[1][1], 'label', labelDict[p[1][1]][1])
        labelDict[p[1][1]][0] = True
        newl = labelDict[p[1][1]][1]
    else:
        newl = new_label()
        scopeDict[0].insert(p[1][1], "label")
        scopeDict[0].updateArgList(p[1][1], 'label', newl)
        labelDict[p[1][1]] = [True, newl]
    p[0] = p[3]
    p[0].code = [['label', newl]] + p[0].code


def p_label(p):
    ''' Label : IDENTIFIER '''
    # print(inspect.stack()[0][3])
    p[0] = ["Label", p[1]]


def p_expression_stmt(p):
    ''' ExpressionStmt : Expression '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].code = p[1].code


def p_inc_dec(p):
    ''' IncDecStmt : Expression INC
                    | Expression DEC '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].code = p[1].code
    p[0].code.append([p[2], p[1].placelist[0]])


def p_assignment(p):
    ''' Assignment : ExpressionList assign_op ExpressionList'''
    global scopeDict
    # print(inspect.stack()[0][3])
    if len(p[1].placelist) != len(p[3].placelist):
        raise ValueError("Number of expressions are not equal")
    p[0] = IRNode()
    p[0].code = p[1].code
    p[0].code += p[3].code
    for x in range(len(p[1].placelist)):
        p[0].code.append([p[2][1][1], p[1].placelist[x], p[3].placelist[x]])
        if p[1].extra['AddrList'][x] != 'None':
            p[0].code.append(
                ['load', p[1].extra['AddrList'][x], p[1].placelist[x]])
    # TODO type checking
    # for i in range(0, len(p[1].typeList)):
    #     print('\tComparing types', p[1].typeList[i], p[3].typeList[i], p[1].typeList[i] == p[3].typeList[i])
    #     if p[1].typeList[i] != p[3].typeList[i]:
    #         raise ValueError("Type of " + str(p[1]) + " & " + str(p[3]) + " is not same")
    # print('Type Checking:', p[3], scopeDict[0].getInfo(p[3].placelist[0]))

    
    # TODO typelist check required
    for i in range(0, len(p[1].typeList)):
        currType = p[1].typeList[i]
        comp = p[3].typeList[i]
        if comp.startswith('lit'):
            comp = comp[3:]
        if currType.startswith('lit'):
            currType = currType[3:]
        print('\tComparing types', currType, comp, isValidAssignment(currType, comp))
        if not isValidAssignment(currType, comp):
            raise ValueError("Type of " + comp + " cannot be assigned to " + currType)
        print('Type Checking:', p[3], currType)


def p_assign_op(p):
    ''' assign_op : AssignOp'''
    # print(inspect.stack()[0][3])
    p[0] = ["assign_op", p[1]]


def p_AssignOp(p):
    ''' AssignOp : PLUS_ASSIGN
                 | MINUS_ASSIGN
                 | MULT_ASSIGN
                 | DIV_ASSIGN
                 | MOD_ASSIGN
                 | AND_ASSIGN
                 | OR_ASSIGN
                 | XOR_ASSIGN
                 | LSHIFT_ASSIGN
                 | RSHIFT_ASSIGN
                 | ASSIGN '''
    # print(inspect.stack()[0][3])
    p[0] = ["AssignOp", p[1]]


def p_if_statement(p):
    ''' IfStmt : IF Expression CreateScope Block EndScope ElseOpt'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].code = p[2].code
    label1 = new_label()
    newVar = new_temp()
    scopeDict[currentScope].insert(newVar, 'int_t')
    scopeDict[currentScope].updateArgList(newVar, 'offset', scopeDict[currentScope].currOffset + 4)
    scopeDict[currentScope].currOffset += 4
    p[0].code += [['=', newVar, p[2].placelist[0]]]
    newVar2 = new_temp()
    scopeDict[currentScope].insert(newVar2, 'int_t')
    scopeDict[currentScope].updateArgList(newVar2, 'offset', scopeDict[currentScope].currOffset + 4)
    scopeDict[currentScope].currOffset += 4
    p[0].code += [['=', newVar2, '1']]
    p[0].code += [['-', newVar, newVar2, newVar]]
    p[0].code += [['ifgoto', newVar, label1]]
    p[0].code += p[4].code
    label2 = new_label()
    p[0].code += [['goto', label2]]
    p[0].code += [['label', label1]]
    p[0].code += p[6].code
    p[0].code += [['label', label2]]


def p_SimpleStmtOpt(p):
    ''' SimpleStmtOpt : SimpleStmt SEMICOLON
                        | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = ["SimpleStmtOpt", p[1], ";"]
    else:
        p[0] = ["SimpleStmtOpt", p[1]]


def p_else_opt(p):
    ''' ElseOpt : ELSE IfStmt
                | ELSE CreateScope Block EndScope
                | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = p[1]
# ----------------------------------------------------------------


# ----------- SWITCH STATEMENTS ---------------------------------
def p_switch_statement(p):
    ''' SwitchStmt : ExprSwitchStmt
                    | TypeSwitchStmt '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_expr_switch_stmt(p):
    ''' ExprSwitchStmt : SWITCH ExpressionOpt LEFT_BRACES ExprCaseClauseRep RIGHT_BRACES'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]
    defaultLabel = None
    labnew = new_label()
    p[0].code += [['goto', labnew]]
    p[0].code += p[6].code
    p[0].code += [['label', labnew]]
    p[0].code += p[6].extra['exprList']
    for i in range(len(p[6].extra['labelList'])):
        if p[6].extra['labelType'][i] == 'default':
            defaultLabel = p[6].extra['labelList'][i]
        else:
            varNew = new_temp()
            scopeDict[currentScope].insert(varNew, 'int_t')
            scopeDict[currentScope].updateArgList(varNew, 'offset', scopeDict[currentScope].currOffset + 4)
            scopeDict[currentScope].currOffset += 4
            p[0].code += [['==', varNew, p[2].placelist[0], p[6].placelist[i]]]
            p[0].code += [['ifgoto', varNew, p[6].extra['labelList'][i]]]
    if defaultLabel is not None:
        p[0].code += [['goto', defaultLabel]]
    else:
        l = new_label()
        p[0].code += [['goto', l]]
        p[0].code += [['label', l]]
    p[0].code += [['label', p[5].extra['end']]]


def p_start_switch(p):
    ''' StartSwitch : '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    label2 = new_label()
    scopeDict[currentScope].updateExtra('endFor', label2)
    p[0].extra['end'] = label2


def p_expr_case_clause_rep(p):
    ''' ExprCaseClauseRep : ExprCaseClauseRep ExprCaseClause
                            | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[1]
        p[0].code += p[2].code
        p[0].placelist += p[2].placelist
        p[0].extra['labelList'] += p[2].extra['labelList']
        p[0].extra['labelType'] += p[2].extra['labelType']
        p[0].extra['exprList'] += p[2].extra['exprList']
    else:
        p[0] = p[1]
        p[0].extra['labelList'] = []
        p[0].extra['labelType'] = []
        p[0].extra['exprList'] = [[]]


def p_expr_case_clause(p):
    ''' ExprCaseClause : ExprSwitchCase COLON StatementList'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    label = new_label()
    p[0].code = [['label', label]]
    p[0].code += p[3].code
    p[0].extra['labelList'] = [label]
    lab = find_label('endFor')
    p[0].code.append(['goto', lab])
    p[0].extra['exprList'] = p[1].extra['exprList']
    p[0].placelist = p[1].placelist
    p[0].extra['labelType'] = p[1].extra['labelType']


def p_expr_switch_case(p):
    ''' ExprSwitchCase : CASE ExpressionList
                        | DEFAULT '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[2]
        p[0].extra['labelType'] = ['case']
        p[0].extra['exprList'] = p[2].code
    else:
        p[0] = IRNode()
        p[0].extra['labelType'] = ['default']
        p[0].placelist = ['heya']
        p[0].extra['exprList'] = [[]]


def p_type_switch_stmt(p):
    ''' TypeSwitchStmt : SWITCH SimpleStmtOpt TypeSwitchGuard LEFT_BRACES TypeCaseClauseOpt RIGHT_BRACES'''
    # print(inspect.stack()[0][3])
    p[0] = ["TypeSwitchStmt", "switch", p[2], p[3], "{", p[5], "}"]


def p_type_switch_guard(p):
    ''' TypeSwitchGuard : IdentifierOpt PrimaryExpr DOT LEFT_PARANTHESIS TYPE RIGHT_PARANTHESIS '''
    # print(inspect.stack()[0][3])

    p[0] = ["TypeSwitchGuard", p[1], p[2], ".", "(", "type", ")"]


def p_identifier_opt(p):
    ''' IdentifierOpt : IDENTIFIER QUICK_ASSIGN
                      | epsilon '''
    # print(inspect.stack()[0][3])

    if len(p) == 3:
        p[0] = ["IdentifierOpt", p[1], ":="]
    else:
        p[0] = ["IdentifierOpt", p[1]]


def p_type_case_clause_opt(p):
    ''' TypeCaseClauseOpt : TypeCaseClauseOpt TypeCaseClause
                          | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = ["TypeCaseClauseOpt", p[1], p[2]]
    else:
        p[0] = ["TypeCaseClauseOpt", p[1]]


def p_type_case_clause(p):
    ''' TypeCaseClause : TypeSwitchCase COLON StatementList'''
    # print(inspect.stack()[0][3])
    p[0] = ["TypeCaseClause", p[1], ":", p[3]]


def p_type_switch_case(p):
    ''' TypeSwitchCase : CASE TypeList
                       | DEFAULT '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = ["TypeSwitchCase", p[1], p[2]]
    else:
        p[0] = ["TypeSwitchCase", p[1]]


def p_type_list(p):
    ''' TypeList : Type TypeRep'''
    # print(inspect.stack()[0][3])
    p[0] = ["TypeList", p[1], p[2]]


def p_type_rep(p):
    ''' TypeRep : TypeRep COMMA Type
                | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = ["TypeRep", p[1], ",", p[3]]
    else:
        p[0] = ["TypeRep", p[1]]

# -----------------------------------------------------------


# --------- FOR STATEMENTS AND OTHERS (MANDAL) ---------------
def p_for(p):
    '''ForStmt : FOR CreateScope ConditionBlockOpt Block EndScope'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    label1 = p[3].extra['before']
    p[0].code = p[3].code + p[4].code + p[3].extra['afterCode']
    p[0].code += [['goto', label1]]
    label2 = p[3].extra['after']
    p[0].code += [['label', label2]]


def p_conditionblockopt(p):
    '''ConditionBlockOpt : epsilon
                | Condition
                | ForClause'''
    #  | RangeClause'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_condition(p):
    '''Condition : Expression '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_forclause(p):
    '''ForClause : SimpleStmt SEMICOLON ConditionOpt SEMICOLON SimpleStmt'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    label1 = new_label()
    p[0].code += [['label', label1]]
    p[0].extra['before'] = label1
    p[0].code += p[3].code
    label2 = new_label()
    scopeDict[currentScope].updateExtra('beginFor', label1)
    scopeDict[currentScope].updateExtra('endFor', label2)

    p[0].extra['after'] = label2
    if len(p[3].placelist) != 0:
        newVar = new_temp()
        newVar2 = new_temp()
        scopeDict[currentScope].insert(newVar, 'int_t')
        scopeDict[currentScope].updateArgList(newVar, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        scopeDict[currentScope].insert(newVar2, 'int_t')
        scopeDict[currentScope].updateArgList(newVar2, 'offset', scopeDict[currentScope].currOffset + 4)
        scopeDict[currentScope].currOffset += 4
        p[0].code += [['=', newVar, p[3].placelist[0]], ['=', newVar2, '1'],
                      ['-', newVar, newVar2, newVar], ['ifgoto', newVar, label2]]
    p[0].extra['afterCode'] = p[5].code


def p_conditionopt(p):
    '''ConditionOpt : epsilon
            | Condition '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]


def p_expression_ident_listopt(p):
    '''ExpressionIdentListOpt : epsilon
               | ExpressionIdentifier'''
    # print(inspect.stack()[0][3])
    p[0] = ["ExpressionIdentListOpt", p[1]]

def p_expressionidentifier(p):
    '''ExpressionIdentifier : ExpressionList ASSIGN'''
    # print(inspect.stack()[0][3])
    if p[2] == "=":
        p[0] = ["ExpressionIdentifier", p[1], "="]
    else:
        p[0] = ["ExpressionIdentifier", p[1], ":="]

def p_return(p):
    '''ReturnStmt : RETURN ExpressionListPureOpt'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]
    if len(p[2].placelist) != 0:
        p[0].code.append(["retint", p[2].placelist[0]])
    else:
        p[0].code.append(["retvoid"])

def p_expressionlist_pure_opt(p):
    '''ExpressionListPureOpt : ExpressionList
                            | epsilon'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]

def p_break(p):
    '''BreakStmt : BREAK LabelOpt'''
    # print(inspect.stack()[0][3])
    if type(p[2]) is list:
        if p[2][1] not in labelDict:
            newl = new_label()
            labelDict[p[2][1]] = [False, newl]
        p[0] = IRNode()
        p[0].code = [['goto', labelDict[p[2][1]][1]]]
    else:
        lab = find_label('endFor')
        p[0] = IRNode()
        p[0].code.append(['goto', lab])

def p_continue(p):
    '''ContinueStmt : CONTINUE LabelOpt'''
    # print(inspect.stack()[0][3])
    if type(p[2]) is list:
        if p[2][1] not in labelDict:
            newl = new_label()
            labelDict[p[2][1]] = [False, newl]
        p[0] = IRNode()
        p[0].code = [['goto', labelDict[p[2][1]][1]]]
    else:
        lab = find_label('beginFor')
        p[0] = IRNode()
        p[0].code.append(['goto', lab])

def p_labelopt(p):
    '''LabelOpt : Label
            | epsilon '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]

def p_goto(p):
    '''GotoStmt : GOTO Label '''
    # print(inspect.stack()[0][3])
    if p[2][1] not in labelDict:
        newl = new_label()
        labelDict[p[2][1]] = [False, newl]
    p[0] = IRNode()
    p[0].code = [['goto', labelDict[p[2][1]][1]]]
# -----------------------------------------------------------

# ----------------  SOURCE FILE --------------------------------
def p_source_file(p):
    '''SourceFile : PackageClause SEMICOLON ImportDeclRep TopLevelDeclRep'''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    p[0].code += p[3].code
    p[0].code += p[4].code

def p_import_decl_rep(p):
    '''ImportDeclRep : epsilon
            | ImportDeclRep ImportDecl SEMICOLON'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[2].code
    else:
        p[0] = p[1]

def p_toplevel_decl_rep(p):
    '''TopLevelDeclRep : TopLevelDeclRep TopLevelDecl SEMICOLON
                        | epsilon'''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].code += p[2].code
    else:
        p[0] = p[1]
# --------------------------------------------------------

# ---------- PACKAGE CLAUSE --------------------
def p_package_clause(p):
    '''PackageClause : PACKAGE PackageName'''
    # print(inspect.stack()[0][3])
    p[0] = p[2]

def p_package_name(p):
    '''PackageName : IDENTIFIER'''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].idList.append(str(p[1]))
    if isUsed(p[1], "."):
        raise NameError("Variable " + p[1] + " already defined")
    else:
        scopeDict[0].insert(p[1], "package")
# -----------------------------------------------

# --------- IMPORT DECLARATIONS ---------------
def p_import_decl(p):
    '''ImportDecl : IMPORT ImportSpec
            | IMPORT LEFT_PARANTHESIS ImportSpecRep RIGHT_PARANTHESIS '''
    # print(inspect.stack()[0][3])
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = IRNode()

def p_import_spec_rep(p):
    ''' ImportSpecRep : ImportSpecRep ImportSpec SEMICOLON
                | epsilon '''
    # print(inspect.stack()[0][3])
    if len(p) == 4:
        p[0] = p[1]
        p[0].idList += p[2].idList
    else:
        p[0] = p[1]

def p_import_spec(p):
    ''' ImportSpec : PackageNameDotOpt ImportPath '''
    # print(inspect.stack()[0][3])
    p[0] = p[1]
    if len(p[1].idList) != 0:
        p[0].idList = p[1].idList[0] + " " + p[2].idList[0]
    else:
        p[0].idList += p[2].idList

def p_package_name_dot_opt(p):
    ''' PackageNameDotOpt : DOT
                            | PackageName
                            | epsilon'''
    # print(inspect.stack()[0][3])
    if p[1] == '.':
        p[0] = IRNode()
        p[0].idList.append(".")
    else:
        p[0] = p[1]

def p_import_path(p):
    ''' ImportPath : STRING '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    p[0].idList.append(str(p[1]))
# -------------------------------------------------------

def p_empty(p):
    '''epsilon : '''
    # print(inspect.stack()[0][3])
    p[0] = IRNode()
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
    exit()

# Build the parser
parser = yacc.yacc()

try:
    s = data
    print(s)
except EOFError:
    print("khatam bc")
if not s:
    print("bas kar")


result = parser.parse(s)
filename = './results/' + input_file.split('/')[-1] + ".ir"
t = open(filename, 'w+')

# print(result)
# print("-------------------------------------")
# print(rootNode.code)
counter = 1
# for code in rootNode.code:
#     t.write(str(counter) + ', ')
#     for x in range(0, len(code) - 1):
#         t.write(str(code[x]) + ', ')
#     t.write(str(code[-1]) + '\n')
#     counter = counter + 1
# t.close()

sys.stdout = open(filename, "w+")

def printList(node):
    global counter
    for i in range(0, len(rootNode.code)):
        if len(rootNode.code[i]) > 0:
            toPrint = ""
            # toPrint += str(counter)
            for j in range(0, len(rootNode.code[i])):
                toPrint += ", " + str(rootNode.code[i][j])
            print(toPrint[1:].strip())
            counter += 1

printList(rootNode)

for s in scopeDict:
    print(scopeDict[s])

var_offset ,max_size=get_offset(scopeDict) 
print(var_offset,max_size)
# print(get_max_offset(scopeDict,var_offset))

sys.stdout = sys.__stdout__
IR = rootNode.code

# S = get_offset(scopeDict)
# print(S)