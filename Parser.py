from Tree import *

#take tokens return tree 
def parse(tokens):
    return program(tokens)

def program(tokens):
    index = 0
    temp, index = block(tokens, index)
    if tokens[index].type != 'PERIOD':
        raise Exception("INVALID PROGRAM")
    index += 1
    if len(tokens) != index:
        raise Exception('INVALID PROGRAM')
    return Program(temp)

def block(tokens, index):
    constant_list, index = const_decl(tokens, index)
    var_list, index = var_decl(tokens, index)
    procedure_list, index = proc_decl(tokens, index)
    localStatement, index = statement(tokens, index)
    return Block(constant_list, var_list, procedure_list, localStatement), index

def const_decl(tokens, index):
    if tokens[index].type != 'CONST':
        return Const_Decl([]), index
    index += 1
    constant_list = []
    while True:
        if tokens[index].type == 'IDENTIFIER' and tokens[index+1].type == 'EQUALS' and tokens[index+2].type == 'NUMBER':
            constant_list.append(Constant(Identifier(tokens[index]), tokens[index+2]))
            index += 3
        else:
            raise Exception('INVALID PROGRAM')
        if tokens[index].type == ';':
            index += 1
            return Const_Decl(constant_list, index)
        if tokens[index].type == ',':
            index += 1
        else:
            raise Exception('INVALID PROGRAM')
    
def var_decl(tokens, index):
    if tokens[index].type != 'VAR':
        return Var_Decl([]), index
    index += 1
    var_list = []
    while True:
        if tokens[index].type == 'IDENTIFIER':
            var_list(Identifier(tokens[index]))
        else:
            raise Exception('INVALID PROGRAM')
        index+=1
        if tokens[index].type == ';':
            index += 1
            return Var_Decl(var_list, index)
        if tokens[index].type == ',':
            index += 1
        else:
            raise Exception('INVALID PROGRAM')
    
def proc_decl(tokens, index):
    procedure_list = []
    while True:
        if tokens[index].type != 'PROCEDURE':
            return proc_decl(procedure_list), index
        index += 1
        if tokens[index].type == 'IDENTIFIER' and tokens[index+1].type == 'SEMICOLON':
            ident = Identifier(tokens[index])
            index += 2
            temp, index = block(tokens, index)
            procedure_list.append(Procedure(ident, temp))
            if tokens[index].type != 'SEMICOLON':
                raise Exception('INVALID PROGRAM')
            index += 1
        else:
            raise Exception('INVALID PROGRAM')

def statement(tokens, index):
    if tokens[index].type == 'IDENTIFIER':
        if tokens[index+1].type == 'Assign':
            ident = tokens[index]
            exp, index = expression(tokens, index+2)
            return Assignment(ident, exp), index
        else:
            raise Exception('Invalid Program')
    if tokens[index].type == 'CALL':
        index += 1
        if tokens[index].type == 'IDENTIFIER':
            return Call(tokens[index]), index+1
    if tokens[index].type == 'BEGIN':
        index +=1
        stmt_list = []
        stmt, index = statement(tokens, index)
        stmt_list.append(stmt)
        while True:
            if tokens[index].type != 'SEMICOLON':
                break
            index += 1
            stmt, index = statement(tokens, index)
            stmt_list.append(stmt)
        if tokens[index].type != 'END':
            raise Exception('INVALID PROGRAM')
        index += 1
        return Executable(stmt_list), index
    if tokens[index].type == 'IF':
        index+=1
        cond, index = condition(tokens, index)
        if tokens[index].type != 'THEN':
            raise Exception('INVALID PROGRAM')
        index += 1
        stmt, index = statement(tokens, index)
        return Conditional(cond, stmt), index
    if tokens[index].type == 'WHILE':
        index+=1
        cond, index = condition(tokens, index)
        if tokens[index].type != 'DO':
            raise Exception('INVALID PROGRAM')
        index += 1
        stmt, index = statement(tokens, index)
        return Loop(cond, stmt), index
    return Empty(), index+1

def condition(tokens, index):
    if tokens[index].type == 'ODD':
        index += 1
        temp, index = expression(tokens,index)
        return Odd(temp), index
    left, index = expression(tokens, index)
    if tokens[index].literal not in ['=', '#', '<','>', '<=', '>=']:
        raise Exception('INVALID PROGRAM')
    relation = tokens[index]
    index += 1
    right, index = expression(tokens, index)
    return BinaryCondition(left, relation, right)