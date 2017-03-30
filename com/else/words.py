from com.ListModel import *
from com.Reader import *

list = ListModel('words')
text = Reader('/home/dan/Programming/Python/Project_Y/com/else/Words')
words = []

def init():
    counter = 0
    header = ''
    while True:
        s = text.nextLine()
        if s == '#__END__':
            print(counter)
            break
        if s != '----------' and '#' not in s:
            counter += 1
            words.append(s)
init()
for word in words:
    list.createEntry(word)


