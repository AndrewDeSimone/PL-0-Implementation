class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    def __str__(self):
        return f'({self.type}, {self.literal})'
    
    def __eq__(self, other):
        return self.type == other.type and self.literal == other.literal