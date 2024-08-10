class CharacterStream:

    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.text = ''
        
        for i in file.readlines():
            self.text += i

        self.text = self.text.replace('\n', '')

        self.text = [i for i in self.text]

        file.close()

    def hasNext(self):
        return len(self.text) > 0
    
    def next(self):
        return self.text.pop(0)
    
    def peek(self):
        return self.text[0]