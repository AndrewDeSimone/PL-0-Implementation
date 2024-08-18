#takes pl0 file and returns character list of file
def filetotext(fileName):
    file = open(fileName, 'r')
    text = ''
    
    for i in file.readlines():
        text += i

    text = text.replace('\n', ' ')

    text = [i for i in text]

    file.close()

    return text