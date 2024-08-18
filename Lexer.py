from Token import Token

#takes character list and returns tokens
def scan(text):
    tokens = []
    text = purgespaces(text)
    while len(text)>0:
        if text[0] == '.':
            tokens.append(Token('PERIOD', '.'))
            text.pop(0)
        elif text[0] == '=':
            tokens.append(Token('EQUALS', '='))
            text.pop(0)
        elif text[0] == ':':
            text.pop(0)
            if len(text)==0:
                raise Exception('INVALID TOKEN')
            if text[0] =='=':
                tokens.append(Token('ASSIGN', ':='))
                text.pop(0)
            else:
                raise Exception('INVALID TOKEN')
        elif text[0] == ',':
            tokens.append(Token('COMMA', ','))
            text.pop(0)
        elif text[0] == ';':
            tokens.append(Token('SEMICOLON', ';'))
            text.pop(0)
        elif text[0] == '?':
            tokens.append(Token('QUESTION', '?'))
            text.pop(0)
        elif text[0] == '!':
            tokens.append(Token('BANG', '!'))
            text.pop(0)
        elif text[0] == '#':
            tokens.append(Token('POUND', '#'))
            text.pop(0)
        elif text[0] == '>':
            text.pop(0)
            if len(text) != 0 and text[0] == '=':
                text.pop(0)
                tokens.append(Token('GEQ', '>='))
            else:
                tokens.append(Token('GE', '>'))
        elif text[0] == '<':
            text.pop(0)
            if len(text) != 0 and text[0] == '=':
                text.pop(0)
                tokens.append(Token('LEQ', '<='))
            else:
                tokens.append(Token('LE', '<'))
        elif text[0] == '+':
            tokens.append(Token('PLUS', '+'))
            text.pop(0)
        elif text[0] == '-':
            tokens.append(Token('MINUS', '-'))
            text.pop(0)
        elif text[0] == '*':
            tokens.append(Token('ASTERIK', '*'))
            text.pop(0)
        elif text[0] == '/':
            tokens.append(Token('SLASH', '/'))
            text.pop(0)
        elif text[0] == '(':
            tokens.append(Token('LEFTPAREN', '('))
            text.pop(0)
        elif text[0] == ')':
            tokens.append(Token('RIGHTPAREN', ')'))
            text.pop(0)
        elif text[0].isdigit():
            number = text[0]
            text.pop(0)
            while len(text)!=0 and text[0].isdigit():
                number += text[0]
                text.pop(0)
            tokens.append(Token('NUMBER', int(number)))
        elif text[0].isalpha():
            word = text[0]
            text.pop(0)
            while len(text)!=0 and text[0].isalpha():
                word += text[0]
                text.pop(0)
            if word in ['CONST', 'VAR', 'PROCEDURE', 'CALL', 'BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'ODD']:
                tokens.append(Token(word, word))
            else:
                tokens.append(Token('IDENTIFIER', word))
        else:
            raise Exception('INVALID TOKEN')
        text = purgespaces(text)
    return tokens

#removes spaces from beginning of text
def purgespaces(text):
    while len(text)>0:
        if text[0] == ' ':
            text.pop(0)
        else:
            return text
    return text