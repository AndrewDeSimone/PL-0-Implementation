class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    def __str__(self):
        return f'({self.type}, {self.literal})'