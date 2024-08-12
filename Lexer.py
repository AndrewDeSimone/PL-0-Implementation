from CharacterStream import CharacterStream
from Token import Token

class Lexer:

    def __init__(self, fileName):
        self.stream = CharacterStream(fileName)
    
    def isEnd(self):
        self.stream.purgeSpaces()
        return self.stream.isEnd()

    def next(self):
        if self.stream.peek() == '.':
            return Token('PERIOD', self.stream.pop())
        elif self.stream.peek() == '=':
            return Token('EQUALS', self.stream.pop())
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
            return Token('LESSTHAN', self.stream.pop())
        elif self.stream.peek() == '>':
            return Token('GREATERTHAN', self.stream.pop())
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
        else:
            raise Exception('Lexing Error: not a valid token')