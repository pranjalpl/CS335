#!/usr/bin/env python

import sys
import ply.lex as lex
import re
import argparse

tokens = (
    'STRUCT', 'FUNC', 'CONST', 'TYPE', 'VAR', 'IF', 'ELSE', 'SWITCH', 'CASE', 'DEFAULT', 'FOR', 'RANGE', 'RETURN', 'BREAK', 'CONTINUE', 'GOTO', 'PACKAGE', 'IMPORT', 'INT_T', 'FLOAT_T', 'UINT_T',
    'COMPLEX_T', 'RUNE_T', 'BOOL_T', 'STRING_T', 'TYPECAST', 'ADD', 'SUB', 'MULT', 'DIV', 'MOD', 'ASSIGN', 'AND', 'LOG_AND', 'INC', 'DEC', 'LEFT_PARANTHESIS', 'RIGHT_PARANTHESIS', 'OR', 'XOR',
    'LSHIFT', 'RSHIFT', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'LOG_OR', 'EQ', 'LT', 'GT',
    'NOT', 'NEQ', 'LEQ', 'GEQ', 'QUICK_ASSIGN', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACES', 'RIGHT_BRACES', 'COMMA', 'DOT', 'SEMICOLON', 'COLON', 'INTEGER', 'OCTAL', 'HEX', 'FLOAT', 'STRING', 'IMAGINARY',
    'RUNE', 'IDENTIFIER', 'PRINT', 'SCAN', 'MALLOC'
)

keywords = {'STRUCT', 'FUNC', 'CONST', 'TYPE', 'VAR', 'IF', 'ELSE', 'SWITCH', 'CASE', 'PRINT', 'SCAN',
            'DEFAULT', 'FOR', 'RANGE', 'RETURN', 'BREAK', 'CONTINUE', 'GOTO', 'PACKAGE', 'IMPORT', 'INT_T', 'FLOAT_T', 'UINT_T', 'COMPLEX_T', 'RUNE_T', 'BOOL_T', 'STRING_T', 'TYPECAST', 'MALLOC'}

reserved = {}
for r in keywords:
	reserved[r.lower()] = r

# Token definitions

t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
t_ignore = ' \t'
t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_ASSIGN = r'='
t_AND = r'&'
t_LOG_AND = r'&&'
t_INC = r'\+\+'
t_DEC = r'--'
t_LEFT_PARANTHESIS = r'\('
t_RIGHT_PARANTHESIS = r'\)'
t_OR = r'\|'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULT_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = r'\^='
t_LSHIFT_ASSIGN = r'<<='
t_RSHIFT_ASSIGN = r'>>='
t_LOG_OR = r'\|\|'
t_EQ = r'=='
t_LT = r'<'
t_GT = r'>'
t_NOT = r'!'
#t_UNOT = r'!'
t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_QUICK_ASSIGN = r':='
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACES = r'\{'
t_RIGHT_BRACES = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_SEMICOLON = r';'
t_COLON = r':'

# Integer based reg variables
decimal_lit = "(0|([1-9][0-9]*))"
octal_lit = "(0[0-7]*)"
hex_lit = "(0x|0X)[0-9a-fA-F]+"

# Float based reg variables
float_lit = "[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?"

# string_lit = """("[^"]*")|(\'[^\']*\')"""
string_lit = """("[^"]*")"""
imaginary_lit = "(" + decimal_lit + "|" + float_lit + ")i"

rune_lit = "\'(.|(\\[abfnrtv]))\'"

identifier_lit = "[_a-zA-Z]+[a-zA-Z0-9_]*"

# t_PRINT = r'print'
# t_SCAN = r'scan'

@lex.TOKEN(identifier_lit)
def t_IDENTIFIER(t):
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


@lex.TOKEN(rune_lit)
def t_RUNE(t):
    t.value = ord(t.value[1:-1])
    return t


@lex.TOKEN(string_lit)
def t_STRING(t):
    t.value = t.value[1:-1]
    return t


@lex.TOKEN(imaginary_lit)
def t_IMAGINARY(t):
    t.value = complex(t.value.replace('i', 'j'))
    return t


@lex.TOKEN(float_lit)
def t_FLOAT(t):
    t.value = float(t.value)
    return t


@lex.TOKEN(hex_lit)
def t_HEX(t):
    t.value = int(t.value, 16)
    return t


@lex.TOKEN(octal_lit)
def t_OCTAL(t):
    t.value = int(t.value, 8)
    return t


@lex.TOKEN(decimal_lit)
def t_INTEGER(t):
    # re.escape(decimal_lit)
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal Character")
    t.lexer.skip(1)


lexer = lex.lex()

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--input", default="../tests/input/test3.go")
args = arg_parser.parse_args()
input_file = args.input

fi=open(input_file,'r')
data=fi.read()
