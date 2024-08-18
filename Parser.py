from Tree import *

#take tokens return tree 
def parse(tokens):
    return program(tokens)

def program(tokens):
    index = 0
    return Program(block(tokens, index))

def block(tokens, index):
    constant_list, index = const_decl(tokens, index)
    var_list, index = var_decl(tokens, index)
    procedure_list, index = proc_decl(tokens, index)
    localStatement, index = statement(tokens, index)
    return Block(constant_list, var_list, procedure_list, localStatement)

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