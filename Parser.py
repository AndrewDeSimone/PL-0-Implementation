from Lexer import Lexer

class Parser:

    def __init__(self, fileName):
        self.lexer = Lexer(fileName)
        self.tokens = self.lexer.getTokens()
        print([str(i) for i in self.tokens])
    
