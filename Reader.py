
class Reader:

    __contents = None
    __pointer = 0

    def __init__(self, file):
        with open(file) as f:
            self.__contents = f.read()

    def getAll(self):
        return self.__contents

    def nextLine(self):
        index = self.__pointer
        self.__pointer += 1
        return self.__contents.split('\n')[index]

