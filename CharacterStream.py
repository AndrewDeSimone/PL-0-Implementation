class CharacterStream:

    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.text = ''
        
        for i in file.readlines():
            self.text += i

        self.text = self.text.replace('\n', '')

        self.text = [i for i in self.text]

        file.close()

    def isEnd(self):
        return not len(self.text) > 0
    
    def pop(self):
        return self.text.pop(0)
    
    def peek(self):
        return self.text[0]
    
    def purgeSpaces(self):
        while len(self.text) > 0:
            if self.peek() == ' ':
                self.pop()
            else:
                return