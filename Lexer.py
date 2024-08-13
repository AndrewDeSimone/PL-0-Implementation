from CharacterStream import CharacterStream
from Token import Token

class Lexer:

    def __init__(self, fileName):
        self.stream = CharacterStream(fileName)
        self.tokens = []
        while not self.isEnd():
            self.tokens.append(self.next())
    
    def getTokens(self):
        return self.tokens
    
    def isEnd(self):
        self.stream.purgeSpaces()
        return self.stream.isEnd()

    def next(self):
        if self.stream.peek() == '.':
            return Token('PERIOD', self.stream.pop())
        elif self.stream.peek() == '=':
            return Token('EQUALS', self.stream.pop())
        elif self.stream.peek() == ':':
            self.stream.pop()
            if self.stream.isEnd() or self.stream.peek() != '=':
                raise Exception('Lexing Error: invalid token')
            self.stream.pop()
            return Token('ASSIGN', ':=')
        elif self.stream.peek() == ',':
            return Token('COMMA', self.stream.pop())
        elif self.stream.peek() == ';':
            return Token('SEMICOLON', self.stream.pop())
        elif self.stream.peek() == '?':
            return Token('QUESTION', self.stream.pop())
        elif self.stream.peek() == '!':
            return Token('BANG', self.stream.pop())
        elif self.stream.peek() == '#':
            return Token('POUND', self.stream.pop())
        elif self.stream.peek() == '<':
            self.stream.pop()
            if self.stream.isEnd() or self.stream.peek() != '=':
                return Token('LE', '<')
            self.stream.pop()
            return Token('LEQ', '<=')
        elif self.stream.peek() == '>':
            self.stream.pop()
            if self.stream.isEnd() or self.stream.peek() != '=':
                return Token('GE', '>')
            self.stream.pop()
            return Token('GEQ', '>=')
        elif self.stream.peek() == '+':
            return Token('PLUS', self.stream.pop())
        elif self.stream.peek() == '-':
            return Token('MINUS', self.stream.pop())
        elif self.stream.peek() == '*':
            return Token('ASTERIK', self.stream.pop())
        elif self.stream.peek() == '/':
            return Token('SLASH', self.stream.pop())
        elif self.stream.peek() == '(':
            return Token('LEFTPAREN', self.stream.pop())
        elif self.stream.peek() == ')':
            return Token('RIGHTPAREN', self.stream.pop())
        elif self.stream.peek().isdigit():
            number = self.stream.pop()
            while not self.stream.isEnd() and self.stream.peek().isdigit():
                number += self.stream.pop()
            return Token('NUMBER', int(number))
        elif self.stream.peek().isalpha():
            identifier = self.stream.pop()
            while not self.stream.isEnd() and self.stream.peek().isalpha():
                identifier += self.stream.pop()
            if identifier in ['CONST', 'VAR', 'PROCEDURE', 'CALL', 'BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'ODD']:
                return Token(identifier, identifier)
            return Token('IDENTIFIER', identifier)
        else:
            raise Exception('Lexing Error: invalid token')