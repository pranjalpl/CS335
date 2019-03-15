# Just a helper function. nothing to see here
def newAssignment(lhs, rhs):
    return {
        "left": lhs,
        "right": rhs
    }

def newBinaryOp(op, lhs, rhs, returns):
    return {
        "op": op,
        "left": lhs,
        "right": rhs,
        "returns": returns
    }
validAssignments = [
    newAssignment('int_t', 'int_t'),
    newAssignment('float_t', 'float_t'),
    newAssignment('complex_t', 'complex_t'),
    newAssignment('string_t', 'string_t'),
    newAssignment('float_t', 'int_t'),
    newAssignment('complex_t', 'int_t'),
    newAssignment('complex_t', 'float_t'),
]

def isValidAssignment(lhs, rhs):
    if lhs.startswith('type'):
        return lhs == rhs
    for x in validAssignments:
        if x['left'] == lhs and x['right'] == rhs:
            return True
    return False

validBinaryOps = [
    newBinaryOp('+', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('+', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('+', 'complex_t', 'complex_t', 'complex_t'),
    newBinaryOp('+', 'string_t', 'string_t', 'string_t'),

    newBinaryOp('+', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('+', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('+', 'int_t', 'complex_t', 'complex_t'),
    newBinaryOp('+', 'complex_t', 'int_t', 'complex_t'),
    newBinaryOp('+', 'float_t', 'complex_t', 'complex_t'),
    newBinaryOp('+', 'complex_t', 'float_t', 'complex_t'),
    
    newBinaryOp('-', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('-', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('-', 'complex_t', 'complex_t', 'complex_t'),

    newBinaryOp('-', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('-', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('-', 'int_t', 'complex_t', 'complex_t'),
    newBinaryOp('-', 'complex_t', 'int_t', 'complex_t'),
    newBinaryOp('-', 'float_t', 'complex_t', 'complex_t'),
    newBinaryOp('-', 'complex_t', 'float_t', 'complex_t'),
    
    newBinaryOp('*', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('*', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('*', 'complex_t', 'complex_t', 'complex_t'),
    newBinaryOp('*', 'string_t', 'int_t', 'string_t'),
    
    newBinaryOp('*', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('*', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('*', 'int_t', 'complex_t', 'complex_t'),
    newBinaryOp('*', 'complex_t', 'int_t', 'complex_t'),
    newBinaryOp('*', 'float_t', 'complex_t', 'complex_t'),
    newBinaryOp('*', 'complex_t', 'float_t', 'complex_t'),
    
    newBinaryOp('/', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('/', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('/', 'complex_t', 'complex_t', 'complex_t'),
    
    newBinaryOp('/', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('/', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('/', 'int_t', 'complex_t', 'complex_t'),
    newBinaryOp('/', 'complex_t', 'int_t', 'complex_t'),
    newBinaryOp('/', 'float_t', 'complex_t', 'complex_t'),
    newBinaryOp('/', 'complex_t', 'float_t', 'complex_t'),

    newBinaryOp('%', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('|', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('>>', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('<<', 'int_t', 'int_t', 'int_t'),

    newBinaryOp('||', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('&&', 'int_t', 'int_t', 'int_t'),
    
    newBinaryOp('==', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('!=', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('<', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('>', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('<=', 'int_t', 'int_t', 'int_t'),
    newBinaryOp('>=', 'int_t', 'int_t', 'int_t'),

    newBinaryOp('==', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('!=', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('<', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('>', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('<=', 'float_t', 'float_t', 'float_t'),
    newBinaryOp('>=', 'float_t', 'float_t', 'float_t'),
    
    newBinaryOp('==', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('!=', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('<', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('>', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('<=', 'int_t', 'float_t', 'float_t'),
    newBinaryOp('>=', 'int_t', 'float_t', 'float_t'),

    newBinaryOp('==', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('!=', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('<', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('>', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('<=', 'float_t', 'int_t', 'float_t'),
    newBinaryOp('>=', 'float_t', 'int_t', 'float_t'),

    newBinaryOp('==', 'string_t', 'string_t', 'string_t'),
    newBinaryOp('!=', 'string_t', 'string_t', 'string_t'),
    newBinaryOp('<', 'string_t', 'string_t', 'string_t'),
    newBinaryOp('>', 'string_t', 'string_t', 'string_t'),
    newBinaryOp('<=', 'string_t', 'string_t', 'string_t'),
    newBinaryOp('>=', 'string_t', 'string_t', 'string_t'),
]

def isValidBinaryOp(op, left, right):
    for i in range(0, len(validBinaryOps)):
        if validBinaryOps[i]['op'] == op and validBinaryOps[i]['left'] == left and validBinaryOps[i]['right'] == right:
            return i
    return -1
