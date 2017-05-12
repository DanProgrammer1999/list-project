from DatabaseManager import *

class EntryModel:
    __id = None
    __text = None
    __state = None
    __tableName = None
    __database = None

    def __init__(self, tableName, entry):
        self.__id = entry[0]
        self.__text = entry[1]
        self.__state = entry[2]
        self.__tableName = tableName

    def getData(self):
        return [self.__id, self.__text, self.__state]

    def getId(self):
        return self.__id

    def getText(self):
        return self.__text

    def getState(self):
        return self.__state

    def setText(self, text):
        self.__database = DatabaseManager.inst()
        self.__database.update(self.__tableName, self.__id, ['text'], [text])
        self.__text = text

    def changeState(self):
        self.__database = DatabaseManager.inst()
        new_state = abs(self.__state - 1)
        self.__database.update(self.__tableName, self.__id, ['state'], [new_state])
        self.__state = new_state
        return new_state