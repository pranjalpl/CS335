import ply.yacc as yacc
import sys
import os
from lexer import *
from pprint import pprint


precedence = (
    ('right','ASSIGN', 'NOT'),
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
    p[0] = ["start", p[1]]
# -------------------------------------------------------


# -----------------------TYPES---------------------------
def p_type(p):
    '''Type : TypeName
            | TypeLit
            | LEFT_PARANTHESIS Type RIGHT_PARANTHESIS'''
    if len(p) == 4:
        p[0] = ["Type", "(", p[2], ")"]
    else:
        p[0] = ["Type", p[1]]

def p_type_name(p):
    '''TypeName : TypeToken
                | QualifiedIdent'''
    p[0] = ["TypeName", p[1]]

def p_type_token(p):
    '''TypeToken : INT_T
                 | FLOAT_T
                 | UINT_T
                 | COMPLEX_T
                 | RUNE_T
                 | BOOL_T
                 | STRING_T
                 | TYPE IDENTIFIER'''
    if len(p) == 2:
        p[0] = ["TypeToken", p[1]]
    else:
        p[0] = ["TypeToken", p[1], p[2]]

def p_type_lit(p):
    '''TypeLit : ArrayType
               | StructType
               | PointerType'''
    p[0] = ["TypeLit", p[1]]

def p_type_opt(p):
    '''TypeOpt : Type
               | epsilon'''
    p[0] = ["TypeOpt", p[1]]
# -------------------------------------------------------





# ------------------- ARRAY TYPE -------------------------
def p_array_type(p):
  '''ArrayType : LEFT_BRACKET ArrayLength RIGHT_BRACKET ElementType'''
  p[0] = ["ArrayType", "[", p[2], "]", p[4]]

def p_array_length(p):
  ''' ArrayLength : Expression '''
  p[0] = ["ArrayLength", p[1]]

def p_element_type(p):
  ''' ElementType : Type '''
  p[0] = ["ElementType", p[1]]

# --------------------------------------------------------


# ----------------- STRUCT TYPE ---------------------------
def p_struct_type(p):
  '''StructType : STRUCT LEFT_BRACES FieldDeclRep RIGHT_BRACES'''
  p[0] = ["StructType", "struct", "{", p[3], "}"]

def p_field_decl_rep(p):
  ''' FieldDeclRep : FieldDeclRep FieldDecl SEMICOLON
                  | epsilon '''
  if len(p) == 4:
    p[0] = ["FieldDeclRep", p[1], p[2], ";"]
  else:
    p[0] = ["FieldDeclRep", p[1]]

def p_field_decl(p):
  ''' FieldDecl : IdentifierList Type TagOpt'''
  p[0] = ["FieldDecl", p[1], p[2], p[3]]

def p_TagOpt(p):
  ''' TagOpt : Tag
             | epsilon '''
  p[0] = ["TagOpt", p[1]]

def p_Tag(p):
  ''' Tag : STRING '''
  p[0] = ["Tag", p[1]]
# ---------------------------------------------------------


# ------------------POINTER TYPES--------------------------
def p_point_type(p):
    '''PointerType : MULT BaseType'''
    p[0] = ["PointerType", "*", p[2]]

def p_base_type(p):
    '''BaseType : Type'''
    p[0] = ["BaseType", p[1]]
# ---------------------------------------------------------


# ---------------FUNCTION TYPES----------------------------
def p_sign(p):
    '''Signature : Parameters ResultOpt'''
    p[0] = ["Signature", p[1], p[2]]

def p_result_opt(p):
    '''ResultOpt : Result
                 | epsilon'''
    p[0] = ["ResultOpt", p[1]]

def p_result(p):
    '''Result : Parameters
              | Type'''
    p[0] = ["Result", p[1]]

def p_params(p):
    '''Parameters : LEFT_PARANTHESIS ParameterListOpt RIGHT_PARANTHESIS'''
    p[0] = ["Parameters", "(", p[2], ")"]

def p_param_list_opt(p):
    '''ParameterListOpt : ParametersList
                             | epsilon'''
    p[0] = ["ParameterListOpt", p[1]]

def p_param_list(p):
    '''ParametersList : Type
                      | IdentifierList Type
                      | ParameterDeclCommaRep'''
    if len(p) == 3:
        p[0] = ["ParametersList", p[1], p[2]]
    else:
        p[0] = ["ParametersList", p[1]]

def p_param_decl_comma_rep(p):
    '''ParameterDeclCommaRep : ParameterDeclCommaRep COMMA ParameterDecl
                             | ParameterDecl COMMA ParameterDecl'''
    p[0] = ["ParameterDeclCommaRep", p[1], ",", p[3]]

def p_param_decl(p):
    '''ParameterDecl : IdentifierList Type
                     | Type'''
    if len(p) == 3:
        p[0] = ["ParameterDecl", p[1], p[2]]
    else:
        p[0] = ["ParameterDecl", p[1]]
# ---------------------------------------------------------


#-----------------------BLOCKS---------------------------
def p_block(p):
    '''Block : LEFT_BRACES StatementList RIGHT_BRACES'''
    p[0] = ["Blocks", "{" , p[2], "}"]

def p_stat_list(p):
    '''StatementList : StatementRep'''
    p[0] = ["StatementList", p[1]]

def p_stat_rep(p):
    '''StatementRep : StatementRep Statement SEMICOLON
                    | epsilon'''
    if len(p) == 4:
        p[0] = ["StatementRep", p[1], p[2], ';']
    else:
        p[0] = ["StatementRep", p[1]]
# -------------------------------------------------------


# ------------------DECLARATIONS and SCOPE------------------------
def p_decl(p):
  '''Declaration : ConstDecl
                 | TypeDecl
                 | VarDecl'''
  p[0] = ["Declaration", p[1]]

def p_toplevel_decl(p):
  '''TopLevelDecl : Declaration
                  | FunctionDecl'''
  p[0] = ["TopLevelDecl", p[1]]
# -------------------------------------------------------


# ------------------CONSTANT DECLARATIONS----------------
def p_const_decl(p):
    '''ConstDecl : CONST ConstSpec
                 | CONST LEFT_PARANTHESIS ConstSpecRep RIGHT_PARANTHESIS'''
    if len(p) == 3:
        p[0] = ["ConstDecl", "const", p[2]]
    else:
        p[0] = ["ConstDecl", "const", '(', p[3], ')']

def p_const_spec_rep(p):
    '''ConstSpecRep : ConstSpecRep ConstSpec SEMICOLON
                    | epsilon'''
    if len(p) == 4:
        p[0] = ["ConstSpecRep", p[1], p[2], ';']
    else:
        p[0] = ["ConstSpecRep", p[1]]

def p_const_spec(p):
    '''ConstSpec : IdentifierList TypeExprListOpt'''
    p[0] = ["ConstSpec", p[1], p[2]]

def p_type_expr_list(p):
    '''TypeExprListOpt : TypeOpt ASSIGN ExpressionList
                       | epsilon'''
    if len(p) == 4:
        p[0] = ["TypeExprListOpt", p[1], "=", p[3]]
    else:
        p[0] = ["TypeExprListOpt", p[1]]

def p_identifier_list(p):
    '''IdentifierList : IDENTIFIER IdentifierRep'''
    p[0] = ["IdentifierList", p[1], p[2]]

def p_identifier_rep(p):
    '''IdentifierRep : IdentifierRep COMMA IDENTIFIER
                     | epsilon'''
    if len(p) == 4:
        p[0] = ["IdentifierRep", p[1], ",", p[3]]
    else:
        p[0] = ["IdentifierRep", p[1]]

def p_expr_list(p):
    '''ExpressionList : Expression ExpressionRep'''
    p[0] = ["ExpressionList", p[1], p[2]]

def p_expr_rep(p):
    '''ExpressionRep : ExpressionRep COMMA Expression
                     | epsilon'''
    if len(p) == 4:
        p[0] = ["ExpressionRep", p[1], ',', p[3]]
    else:
        p[0] = ["ExpressionRep", p[1]]
# -------------------------------------------------------


# ------------------TYPE DECLARATIONS-------------------
def p_type_decl(p):
    '''TypeDecl : TYPE TypeSpec
                | TYPE LEFT_PARANTHESIS TypeSpecRep RIGHT_PARANTHESIS'''
    if len(p) == 5:
        p[0] = ["TypeDecl", "type", "(", p[3], ")"]
    else:
        p[0] = ["TypeDecl", "type", p[2]]

def p_type_spec_rep(p):
    '''TypeSpecRep : TypeSpecRep TypeSpec SEMICOLON
                   | epsilon'''
    if len(p) == 4:
        p[0] = ["TypeSpecRep", p[1], p[2], ";"]
    else:
        p[0] = ["TypeSpecRep", p[1]]

def p_type_spec(p):
    '''TypeSpec : AliasDecl
                | TypeDef'''
    p[0] = ["TypeSpec", p[1]]

def p_alias_decl(p):
    '''AliasDecl : IDENTIFIER ASSIGN Type'''
    p[0] = ["AliasDecl", p[1], '=', p[3]]
# -------------------------------------------------------


# -------------------TYPE DEFINITIONS--------------------
def p_type_def(p):
    '''TypeDef : IDENTIFIER Type'''
    p[0] = ["TypeDef", p[1], p[2]]
# -------------------------------------------------------


# ----------------VARIABLE DECLARATIONS------------------
def p_var_decl(p):
    '''VarDecl : VAR VarSpec
               | VAR LEFT_PARANTHESIS VarSpecRep RIGHT_PARANTHESIS'''
    if len(p) == 3:
        p[0] = ["VarDecl", "var", p[2]]
    else:
        p[0] = ["VarDecl", "var", "(", p[3], ")"]

def p_var_spec_rep(p):
    '''VarSpecRep : VarSpecRep VarSpec SEMICOLON
                  | epsilon'''
    if len(p) == 4:
        p[0] = ["VarSpecRep", p[1], p[2], ";"]
    else:
        p[0] = ["VarSpecRep", p[1]]

def p_var_spec(p):
    '''VarSpec : IdentifierList Type ExpressionListOpt
               | IdentifierList ASSIGN ExpressionList'''
    if p[2] == '=':
        p[0] = ["VarSpec", p[1], "=", p[3]]
    else:
        p[0] = ["VarSpec", p[1], p[2], p[3]]

def p_expr_list_opt(p):
    '''ExpressionListOpt : ASSIGN ExpressionList
                         | epsilon'''
    if len(p) == 3:
        p[0] = ["ExpressionListOpt", "=", p[2]]
    else:
        p[0] = ["ExpressionListOpt", p[1]]
# -------------------------------------------------------


# ----------------SHORT VARIABLE DECLARATIONS-------------
def p_short_var_decl(p):
  ''' ShortVarDecl : IDENTIFIER QUICK_ASSIGN Expression '''
  p[0] = ["ShortVarDecl", p[1], ":=", p[3]]
# -------------------------------------------------------



# ----------------FUNCTION DECLARATIONS------------------
def p_func_decl(p):
    '''FunctionDecl : FUNC FunctionName Function
                    | FUNC FunctionName Signature'''
    p[0] = ["FunctionDecl", "func", p[2], p[3]]

def p_func_name(p):
    '''FunctionName : IDENTIFIER'''
    p[0] = ["FunctionName", p[1]]

def p_func(p):
    '''Function : Signature FunctionBody'''
    p[0] = ["Function", p[1], p[2]]

def p_func_body(p):
    '''FunctionBody : Block'''
    p[0] = ["FunctionBody", p[1]]
# -------------------------------------------------------


# ----------------------OPERAND----------------------------
def p_operand(p):
    '''Operand : Literal
               | OperandName
               | LEFT_PARANTHESIS Expression RIGHT_PARANTHESIS'''
    if len(p) == 2:
        p[0] = ["Operand", p[1]]
    else:
        p[0] = ["Operand", "(", p[2], ")"]

def p_literal(p):
    '''Literal : BasicLit'''
               #| CompositeLit'''
    p[0] = ["Literal", p[1]]

def p_basic_lit(p):
    '''BasicLit : INTEGER
                | OCTAL
                | HEX
                | FLOAT
                | IMAGINARY
                | RUNE
                | STRING'''
    p[0] = ["BasicLit",str(p[1])]

def p_operand_name(p):
    '''OperandName : IDENTIFIER'''
    p[0] = ["OperandName", p[1]]
# ---------------------------------------------------------


# -------------------QUALIFIED IDENTIFIER----------------
def p_quali_ident(p):
    '''QualifiedIdent : IDENTIFIER DOT TypeName'''
    p[0] = ["QualifiedIdent", p[1], ".", p[3]]
# -------------------------------------------------------


# -----------------COMPOSITE LITERALS----------------------
def p_comp_lit(p):
    '''CompositeLit : LiteralType LiteralValue'''
    p[0] = ["CompositeLit", p[1], p[2]]

def p_lit_type(p):
    '''LiteralType : ArrayType
                   | ElementType
                   | TypeName'''
    p[0] = ["LiteralType", p[1]]

def p_lit_val(p):
    '''LiteralValue : LEFT_BRACES ElementListOpt RIGHT_BRACES'''
    p[0] = ["LiteralValue", "{", p[2], "}"]

def p_elem_list_comma_opt(p):
    '''ElementListOpt : ElementList
                           | epsilon'''
    p[0] = ["ElementListOpt", p[1]]

def p_elem_list(p):
    '''ElementList : KeyedElement KeyedElementCommaRep'''
    p[0] = ["ElementList", p[1], p[2]]

def p_key_elem_comma_rep(p):
    '''KeyedElementCommaRep : KeyedElementCommaRep COMMA KeyedElement
                            | epsilon'''
    if len(p) == 4:
        p[0] = ["KeyedElementCommaRep", p[1], ",", p[3]]
    else:
        p[0] = ["KeyedElementCommaRep", p[1]]

def p_key_elem(p):
    '''KeyedElement : Key COLON Element
                    | Element'''
    if len(p) == 4:
        p[0] = ["KeyedElement", p[1], ":", p[3]]
    else:
        p[0] = ["KeyedElement", p[1]]

def p_key(p):
    '''Key : FieldName
           | Expression
           | LiteralValue'''
    p[0] = ["Key", p[1]]

def p_field_name(p):
    '''FieldName : IDENTIFIER'''
    p[0] = ["FieldName", p[1]]

def p_elem(p):
    '''Element : Expression
               | LiteralValue'''
    p[0] = ["Element", p[1]]
# ---------------------------------------------------------


# ------------------PRIMARY EXPRESSIONS--------------------
def p_prim_expr(p):
    '''PrimaryExpr : Operand
                   | PrimaryExpr Selector
                   | Conversion
                   | PrimaryExpr Index
                   | PrimaryExpr Slice
                   | PrimaryExpr TypeAssertion
                   | PrimaryExpr Arguments'''
    if len(p) == 2:
        p[0] = ["PrimaryExpr", p[1]]
    else:
        p[0] = ["PrimaryExpr", p[1], p[2]]

def p_selector(p):
    '''Selector : DOT IDENTIFIER'''
    p[0] = ["Selector", ".", p[2]]

def p_index(p):
    '''Index : LEFT_BRACKET Expression RIGHT_BRACKET'''
    p[0] = ["Index", "[", p[2], "]"]

def p_slice(p):
    '''Slice : LEFT_BRACKET ExpressionOpt COLON ExpressionOpt RIGHT_BRACKET
             | LEFT_BRACKET ExpressionOpt COLON Expression COLON Expression RIGHT_BRACKET'''
    if len(p) == 6:
        p[0] = ["Slice", "[", p[2], ":", p[4], "]"]
    else:
        p[0] = ["Slice", "[", p[2], ":", p[4], ":", p[6], "]"]

def p_type_assert(p):
    '''TypeAssertion : DOT LEFT_PARANTHESIS Type RIGHT_PARANTHESIS'''
    p[0] = ["TypeAssertion", ".", "(", p[3], ")"]

def p_argument(p):
    '''Arguments : LEFT_PARANTHESIS ExpressionListTypeOpt RIGHT_PARANTHESIS'''
    p[0] = ["Arguments", "(", p[2], ")"]

def p_expr_list_type_opt(p):
    '''ExpressionListTypeOpt : ExpressionList
                             | epsilon'''
    if len(p) == 3:
        p[0] = ["ExpressionListTypeOpt", p[1], p[2]]
    else:
        p[0] = ["ExpressionListTypeOpt", p[1]]


def p_expr_list_comma_opt(p):
    '''ExpressionListCommaOpt : COMMA ExpressionList
                              | epsilon'''
    if len(p) == 3:
        p[0] = ["ExpressionListCommaOpt", ",", p[2]]
    else:
        p[0] = ["ExpressionListCommaOpt", p[1]]
# ---------------------------------------------------------


#----------------------OPERATORS-------------------------
def p_expr(p):
    '''Expression : UnaryExpr
                  | Expression BinaryOp Expression'''
    if len(p) == 4:
        p[0] = ["Expression", p[1], p[2], p[3]]
    else:
        p[0] = ["Expression", p[1]]

def p_expr_opt(p):
    '''ExpressionOpt : Expression
                     | epsilon'''
    p[0] = ["ExpressionOpt", p[1]]

def p_unary_expr(p):
    '''UnaryExpr : PrimaryExpr
                 | UnaryOp UnaryExpr
                 | NOT UnaryExpr'''
    if len(p) == 2:
        p[0] = ["UnaryExpr", p[1]]
    elif p[1] == "!":
        p[0] = ["UnaryExpr", "!", p[2]]
    else:
        p[0] = ["UnaryExpr", p[1], p[2]]

def p_binary_op(p):
    '''BinaryOp : LOG_OR
                | LOG_AND
                | RelOp
                | AddMulOp'''
    if p[1] == "||":
        p[0] = ["BinaryOp", "||"]
    elif p[1] == "&&":
        p[0] = ["BinaryOp", "&&"]
    else:
        p[0] = ["BinaryOp", p[1]]

def p_rel_op(p):
    '''RelOp : EQ
             | NEQ
             | LT
             | GT
             | LEQ
             | GEQ'''
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

def p_add_mul_op(p):
    '''AddMulOp : UnaryOp
                | OR
                | XOR
                | DIV
                | MOD
                | LSHIFT
                | RSHIFT'''
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
    p[0] = ["Conversion", p[1], p[2],  "(", p[4], ")"]
# ---------------------------------------------------------






# ---------------- STATEMENTS -----------------------
def p_statement(p):
    '''Statement : Declaration
                 | LabeledStmt
                 | SimpleStmt
                 | ReturnStmt
                 | BreakStmt
                 | ContinueStmt
                 | GotoStmt
                 | Block
                 | IfStmt
                 | SwitchStmt
                 | ForStmt '''
    p[0] = ["Statement", p[1]]



def p_simple_stmt(p):
  ''' SimpleStmt : epsilon
                 | ExpressionStmt
                 | IncDecStmt
                 | Assignment
                 | ShortVarDecl '''
  p[0] = ["SimpleStmt", p[1]]


def p_labeled_statements(p):
  ''' LabeledStmt : Label COLON Statement '''
  p[0] = ["LabeledStmt", p[1], ":", p[3]]

def p_label(p):
  ''' Label : IDENTIFIER '''
  p[0] = ["Label", p[1]]


def p_expression_stmt(p):
  ''' ExpressionStmt : Expression '''
  p[0] = ["ExpressionStmt", p[1]]

def p_inc_dec(p):
  ''' IncDecStmt : Expression INC
                 | Expression DEC '''
  if p[2] == '++':
    p[0] = ["IncDecStmt", p[1], "++"]
  else:
    p[0] = ["IncDecStmt", p[1], "--"]


def p_assignment(p):
  ''' Assignment : ExpressionList assign_op ExpressionList'''
  p[0] = ["Assignment", p[1], p[2], p[3]]

def p_assign_op(p):
  ''' assign_op : AssignOp'''
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
  p[0] = ["AssignOp", p[1]]


def p_if_statement(p):
  ''' IfStmt : IF Expression Block ElseOpt '''
  p[0] = ["IfStmt", "if", p[2], p[3], p[4]]

def p_SimpleStmtOpt(p):
  ''' SimpleStmtOpt : SimpleStmt SEMICOLON
                    | epsilon '''
  if len(p) == 3:
    p[0] = ["SimpleStmtOpt", p[1], ";"]
  else :
    p[0] = ["SimpleStmtOpt", p[1]]

def p_else_opt(p):
  ''' ElseOpt : ELSE IfStmt
              | ELSE Block
              | epsilon '''
  if len(p) == 3:
    p[0] = ["ElseOpt", "else", p[2]]
  else:
    p[0] = ["ElseOpt", p[1]]

# ----------------------------------------------------------------





# ----------- SWITCH STATEMENTS ---------------------------------

def p_switch_statement(p):
  ''' SwitchStmt : ExprSwitchStmt
                 | TypeSwitchStmt '''
  p[0] = ["SwitchStmt", p[1]]


def p_expr_switch_stmt(p):
  ''' ExprSwitchStmt : SWITCH ExpressionOpt LEFT_BRACES ExprCaseClauseRep RIGHT_BRACES'''
  p[0] = ["ExpressionStmt", "switch", p[2], p[3], "{", p[5], "}"]

def p_expr_case_clause_rep(p):
  ''' ExprCaseClauseRep : ExprCaseClauseRep ExprCaseClause
                        | epsilon'''
  if len(p) == 3:
    p[0] = ["ExprCaseClauseRep", p[1], p[2]]
  else:
    p[0] = ["ExprCaseClauseRep", p[1]]

def p_expr_case_clause(p):
  ''' ExprCaseClause : ExprSwitchCase COLON StatementList'''
  p[0] = ["ExprCaseClause", p[1], ":", p[3]]

def p_expr_switch_case(p):
  ''' ExprSwitchCase : CASE ExpressionList
                     | DEFAULT '''
  if len(p) == 3:
    p[0] = ["ExprSwitchCase", "case", p[2]]
  else:
    p[0] = ["ExprSwitchCase", p[1]]

def p_type_switch_stmt(p):
  ''' TypeSwitchStmt : SWITCH SimpleStmtOpt TypeSwitchGuard LEFT_BRACES TypeCaseClauseOpt RIGHT_BRACES'''
  p[0] = ["TypeSwitchStmt", "switch", p[2], p[3],"{", p[5], "}"]


def p_type_switch_guard(p):
  ''' TypeSwitchGuard : IdentifierOpt PrimaryExpr DOT LEFT_PARANTHESIS TYPE RIGHT_PARANTHESIS '''

  p[0] = ["TypeSwitchGuard", p[1], p[2], ".", "(", "type", ")"]

def p_identifier_opt(p):
  ''' IdentifierOpt : IDENTIFIER QUICK_ASSIGN
                    | epsilon '''

  if len(p) == 3:
    p[0] = ["IdentifierOpt", p[1], ":="]
  else:
    p[0] = ["IdentifierOpt", p[1]]

def p_type_case_clause_opt(p):
  ''' TypeCaseClauseOpt : TypeCaseClauseOpt TypeCaseClause
                        | epsilon '''
  if len(p) == 3:
    p[0] = ["TypeCaseClauseOpt", p[1], p[2]]
  else:
    p[0] = ["TypeCaseClauseOpt", p[1]]

def p_type_case_clause(p):
  ''' TypeCaseClause : TypeSwitchCase COLON StatementList'''
  p[0] = ["TypeCaseClause", p[1], ":", p[3]]


def p_type_switch_case(p):
  ''' TypeSwitchCase : CASE TypeList
                     | DEFAULT '''
  if len(p) == 3:
    p[0] = ["TypeSwitchCase", p[1], p[2]]
  else:
    p[0] = ["TypeSwitchCase", p[1]]

def p_type_list(p):
  ''' TypeList : Type TypeRep'''
  p[0] = ["TypeList", p[1], p[2]]

def p_type_rep(p):
  ''' TypeRep : TypeRep COMMA Type
              | epsilon '''
  if len(p) == 4:
    p[0] = ["TypeRep", p[1], ",", p[3]]
  else:
    p[0] = ["TypeRep", p[1]]

# -----------------------------------------------------------






# --------- FOR STATEMENTS AND OTHERS (MANDAL) ---------------
def p_for(p):
  '''ForStmt : FOR ConditionBlockOpt Block'''
  p[0] = ["ForStmt", "for", p[2], p[3]]

def p_conditionblockopt(p):
  '''ConditionBlockOpt : epsilon
             | Condition
             | ForClause
             | RangeClause'''
  p[0] = ["ConditionBlockOpt", p[1]]

def p_condition(p):
  '''Condition : Expression '''
  p[0] = ["Condition", p[1]]

def p_forclause(p):
  '''ForClause : SimpleStmt SEMICOLON ConditionOpt SEMICOLON SimpleStmt'''
  p[0] = ["ForClause", p[1], ";", p[3], ";", p[5]]


def p_conditionopt(p):
  '''ConditionOpt : epsilon
          | Condition '''
  p[0] = ["ConditionOpt", p[1]]


def p_rageclause(p):
  '''RangeClause : ExpressionIdentListOpt RANGE Expression'''
  p[0] = ["RangeClause", p[1], "range", p[3]]

def p_expression_ident_listopt(p):
  '''ExpressionIdentListOpt : epsilon
             | ExpressionIdentifier'''
  p[0] = ["ExpressionIdentListOpt", p[1]]

def p_expressionidentifier(p):
  '''ExpressionIdentifier : ExpressionList ASSIGN'''
  if p[2] == "=":
    p[0] = ["ExpressionIdentifier", p[1], "="]
  else:
    p[0] = ["ExpressionIdentifier", p[1], ":="]

def p_return(p):
  '''ReturnStmt : RETURN ExpressionListPureOpt'''
  p[0] = ["ReturnStmt", "return", p[2]]

def p_expressionlist_pure_opt(p):
  '''ExpressionListPureOpt : ExpressionList
             | epsilon'''
  p[0] = ["ExpressionListPureOpt", p[1]]

def p_break(p):
  '''BreakStmt : BREAK LabelOpt'''
  p[0] = ["BreakStmt", "break", p[2]]

def p_continue(p):
  '''ContinueStmt : CONTINUE LabelOpt'''
  p[0] = ["ContinueStmt", "continue", p[2]]

def p_labelopt(p):
  '''LabelOpt : Label
        | epsilon '''
  p[0] = ["LabelOpt", p[1]]

def p_goto(p):
  '''GotoStmt : GOTO Label '''
  p[0] = ["GotoStmt", "goto", p[2]]
# -----------------------------------------------------------


# ----------------  SOURCE FILE --------------------------------
def p_source_file(p):
    '''SourceFile : PackageClause SEMICOLON ImportDeclRep TopLevelDeclRep'''
    p[0] = ["SourceFile", p[1], ";", p[3], p[4]]

def p_import_decl_rep(p):
  '''ImportDeclRep : epsilon
           | ImportDeclRep ImportDecl SEMICOLON'''
  if len(p) == 4:
    p[0] = ["ImportDeclRep", p[1], p[2], ";"]
  else:
    p[0] = ["ImportDeclRep", p[1]]

def p_toplevel_decl_rep(p):
  '''TopLevelDeclRep : TopLevelDeclRep TopLevelDecl SEMICOLON
                     | epsilon'''
  if len(p) == 4:
    p[0] = ["TopLevelDeclRep", p[1], p[2], ";"]
  else:
    p[0] = ["TopLevelDeclRep", p[1]]
# --------------------------------------------------------


# ---------- PACKAGE CLAUSE --------------------
def p_package_clause(p):
    '''PackageClause : PACKAGE PackageName'''
    p[0] = ["PackageClause", "package", p[2]]


def p_package_name(p):
    '''PackageName : IDENTIFIER'''
    p[0] = ["PackageName", p[1]]
# -----------------------------------------------


# --------- IMPORT DECLARATIONS ---------------
def p_import_decl(p):
  '''ImportDecl : IMPORT ImportSpec
          | IMPORT LEFT_PARANTHESIS ImportSpecRep RIGHT_PARANTHESIS '''
  if len(p) == 3:
    p[0] = ["ImportDecl", "import", p[2]]
  else:
    p[0] = ["ImportDecl", "import", "(", p[3], ")"]

def p_import_spec_rep(p):
  ''' ImportSpecRep : ImportSpecRep ImportSpec SEMICOLON
            | epsilon '''
  if len(p) == 4:
    p[0] = ["ImportSpecRep", p[1], p[2], ";"]
  else:
    p[0] = ["ImportSpecRep", p[1]]

def p_import_spec(p):
  ''' ImportSpec : PackageNameDotOpt ImportPath '''
  p[0] = ["ImportSpec", p[1], p[2]]

def p_package_name_dot_opt(p):
  ''' PackageNameDotOpt : DOT
                        | PackageName
                        | epsilon'''
  if p[1]== '.':
    p[0] = ["PackageNameDotOpt", "."]
  else:
    p[0] = ["PackageNameDotOpt", p[1]]

def p_import_path(p):
  ''' ImportPath : STRING '''
  p[0] = ["ImportPath", p[1]]
# -------------------------------------------------------


def p_empty(p):
  '''epsilon : '''
  p[0] = "epsilon"

# Error rule for syntax errors


def p_error(p):
  print("Syntax error in input!")
  print(p)


# Build the parser
parser = yacc.yacc()

node_id = 0

# def dfs(p,t):
#   global node_id;
#   no_child =len(p)-1
#   parent = node_id
#   parent_name = ""
#   # while(len(p) == 2 and type(p[1]) is list ):
#   #   p = p[1] 
#   for i in range(no_child):
#     if type(p[1+i]) is list:
#       node_id+=1
#       t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
#       # t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
#       t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i][0]))+';\n')
#       # t.write(p[0]+'->'+p[1+i][0]+';')
#       # t.write("\n")
#       dfs(p[1+i],t)
#     else:
#       parent_name+=str(p[1+i])
#       # node_id+=1
#       # t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
#       # t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
#       # t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i]))+';\n')
#       # node_id+=2
#       # t.write(p[0]+'->'+p[1+i]+';')
#       # t.write("\n")
#       # return
#   t.write("Node{}".format(parent)+" [label = \"{}\"]".format(parent_name)+';\n')





def dfs(p,t):
  global node_id;
  no_child =len(p)-1
  parent = node_id
  parent_name = ""
  t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
  for i in range(no_child):
    if type(p[1+i]) is list:
      node_id+=1
      while(len(p[1+i]) == 2 and type(p[i+1][1]) is list ):
        p[i+1] = p[1+i][1]
      if(len(p[1+i]) == 2):
        p[1+i]  = p[1+i][1]
        if(p[i+1]!='epsilon'):
          t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
          t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i]))+';\n')
        continue
      t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
      t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i][0]))+';\n')
      # t.write(p[0]+'->'+p[1+i][0]+';')
      # t.write("\n")
      dfs(p[1+i],t)
    else:
      # parent_name+=str(p[1+i])
      node_id+=1
      t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
      t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
      t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i]))+';\n')
      # node_id+=2
      # t.write(p[0]+'->'+p[1+i]+';')
      # t.write("\n")
      # return
  # t.write("Node{}".format(parent)+" [label = \"{}\"]".format(parent_name)+';\n')


# def dfs(p,t):
#   global node_id;
#   no_child =len(p)-1
#   parent = node_id
#   for i in range(no_child):
#     if type(p[1+i]) is list:
#       node_id+=1
#       t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
#       t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
#       t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i][0]))+';\n')
#       # t.write(p[0]+'->'+p[1+i][0]+';')
#       # t.write("\n")
#       dfs(p[1+i],t)
#     else:
#       node_id+=1
#       t.write("Node{}".format(parent)+'->'+"Node{}".format(node_id)+';\n')
#       t.write("Node{}".format(parent)+" [label = \"{}\"]".format(str(p[0]))+';\n')
#       t.write("Node{}".format(node_id)+" [label = \"{}\"]".format(str(p[1+i]))+';\n')
#       # node_id+=2
#       # t.write(p[0]+'->'+p[1+i]+';')
#       # t.write("\n")
#       # return





try:
  s = data
  print(s)
except EOFError:
  print("khatam bc")
if not s:
  print("bas kar")


result = parser.parse(s)
filename = input_file.split('/')[2] + ".dot"
t =open(filename,'w+')
t.write("digraph G {")
t.write("\n")
dfs(result,t)
t.write("}")
t.write("\n")
t.close()

print(result)