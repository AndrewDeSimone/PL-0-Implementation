import unittest
from Lexer import scan
from Token import Token

def texttolist(text):
        return [i for i in text]

class TestLexer(unittest.TestCase):

    def test_scan(self):
        #period tests
        self.assertEqual(scan(texttolist('.')), [Token('PERIOD', '.')])
        #equals tests
        self.assertEqual(scan(texttolist('=')), [Token('EQUALS', '=')])
        #assign tests
        self.assertEqual(scan(texttolist(':=')), [Token('ASSIGN', ':=')])
        #comma tests
        self.assertEqual(scan(texttolist(',')), [Token('COMMA', ',')])
        #semicolon tests
        self.assertEqual(scan(texttolist(';')), [Token('SEMICOLON', ';')])
        #question tests
        self.assertEqual(scan(texttolist('?')), [Token('QUESTION', '?')])
        #bang tests
        self.assertEqual(scan(texttolist('!')), [Token('BANG', '!')])
        #POUND tests
        self.assertEqual(scan(texttolist('#')), [Token('POUND', '#')])
        #Less Than tests
        self.assertEqual(scan(texttolist('<')), [Token('LE', '<')])
        #LEQ tests
        self.assertEqual(scan(texttolist('<=')), [Token('LEQ', '<=')])
        #Greater Than tests
        self.assertEqual(scan(texttolist('>')), [Token('GE', '>')])
        #LEQ tests
        self.assertEqual(scan(texttolist('>=')), [Token('GEQ', '>=')])
        #PLUS tests
        self.assertEqual(scan(texttolist('+')), [Token('PLUS', '+')])
        #MINUS tests
        self.assertEqual(scan(texttolist('-')), [Token('MINUS', '-')])
        #ASTERIK tests
        self.assertEqual(scan(texttolist('*')), [Token('ASTERIK', '*')])
        #SLASH tests
        self.assertEqual(scan(texttolist('/')), [Token('SLASH', '/')])
        #LEFTPAREN tests
        self.assertEqual(scan(texttolist('(')), [Token('LEFTPAREN', '(')])
        #RIGHTPAREN tests
        self.assertEqual(scan(texttolist(')')), [Token('RIGHTPAREN', ')')])
        #NUMBER tests
        self.assertEqual(scan(texttolist('1')), [Token('NUMBER', 1)])
        self.assertEqual(scan(texttolist('12345')), [Token('NUMBER', 12345)])
        #KEYWORD tests
        self.assertEqual(scan(texttolist('CONST')), [Token('CONST', 'CONST')])
        self.assertEqual(scan(texttolist('VAR')), [Token('VAR', 'VAR')])
        self.assertEqual(scan(texttolist('PROCEDURE')), [Token('PROCEDURE', 'PROCEDURE')])
        self.assertEqual(scan(texttolist('CALL')), [Token('CALL', 'CALL')])
        self.assertEqual(scan(texttolist('BEGIN')), [Token('BEGIN', 'BEGIN')])
        self.assertEqual(scan(texttolist('END')), [Token('END', 'END')])
        self.assertEqual(scan(texttolist('IF')), [Token('IF', 'IF')])
        self.assertEqual(scan(texttolist('THEN')), [Token('THEN', 'THEN')])
        self.assertEqual(scan(texttolist('WHILE')), [Token('WHILE', 'WHILE')])
        self.assertEqual(scan(texttolist('DO')), [Token('DO', 'DO')])
        self.assertEqual(scan(texttolist('ODD')), [Token('ODD', 'ODD')])
        #IDENTIFIER tests
        self.assertEqual(scan(texttolist('dog')), [Token('IDENTIFIER', 'dog')])
