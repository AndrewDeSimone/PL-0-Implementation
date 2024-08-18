class Program:
    def __init__(self, block):
        self.block = block
    
    def accept(self, visitor):
        visitor.visit_program(self)

class Block:
    def __init__(self, const_decl, var_decl, proc_decl, statement):
        self.const_decl = const_decl
        self.var_decl = var_decl
        self.proc_decl = proc_decl
        self.statement = statement
    
    def accept(self, visitor):
        visitor.visit_block(self)

class Const_Decl:
    def __init__(self, constants):
        self.constants = constants
    
    def accept(self, visitor):
        visitor.visit_const_decl(self)

class Constant:
    def __init__(self, identifier, number):
        self.identifier = identifier
        self.number = number
    
    def accept(self, visitor):
        visitor.visit_constant(self)

class Var_Decl:
    def __init__(self, identifiers):
        self.identifiers = identifiers
    
    def accept(self, visitor):
        visitor.visit_var_decl(self)

class Proc_Decl:
    def __init__(self, identifier, block):
        self.identifier = identifier
        self.block = block
    
    def accept(self, visitor):
        visitor.visit_proc_decl(self)

class Statement:
    def __init__(self, statement):
        self.statement = statement
    
    def accept(self, visitor):
        visitor.visit_statement(self)

class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression
    
    def accept(self, visitor):
        visitor.visit_assignment(self)

class Call:
    def __init__(self, identifier):
        self.identifier = identifier
    
    def accept(self, visitor):
        visitor.visit_call(self)

class Executable:
    def __init__(self, statements):
        self.statements = statements
    
    def accept(self, visitor):
        visitor.visit_executable(self)

class Conditional:
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
    
    def accept(self, visitor):
        visitor.visit_conditional(self)

class Loop:
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
    def accept(self, visitor):
        visitor.visit_loop(self)

class Empty:
    def __init__(self):
        pass
    
    def accept(self, visitor):
        visitor.visit_empty(self)

class Odd:
    def __init__(self, expression):
        self.expression = expression
    
    def accept(self, visitor):
        visitor.visit_odd(self)

class BinaryCondition:
    def __init__(self, left, relation, right):
        self.left = left
        self.relation = relation
        self.right = right
    
    def accept(self, visitor):
        visitor.visit_binary_condition(self)

class Expression:
    def __init__(self, terms, adding_operators):
        self.terms = terms
        self.adding_operators = adding_operators
    
    def accept(self, visitor):
        visitor.visit_expression(self)

class Term:
    def __init__(self, factors, multiplying_operators):
        self.factors = factors
        self.multiplying_operators = multiplying_operators

    def accept(self, visitor):
        visitor.visit_term(self)

class Identifier:
    def __init__(self, identifier):
        self.identifier = identifier
    
    def accept(self, visitor):
        visitor.visit_identifier(self)

class Number:
    def __init__(self, number):
        self.number = number
    
    def accept(self, visitor):
        visitor.visit_number(self)
