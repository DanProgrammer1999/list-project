from EntryModel import *

class ListModel:
    __database = None
    __tableName = None
    __elements = []

    def __init__(self, tableName):
        self.__database = DatabaseManager.inst()
        self.__tableName = tableName
        records = self.__database.read_all(self.__tableName)
        for e in records:
            self.__elements.append(EntryModel(self.__tableName, e))

    def getList(self):
        return self.__elements

    def createEntry(self, text):
        col_name = 'text'
        id = self.__database.insert(self.__tableName, [col_name], [text])
        self.__elements.append(EntryModel(self.__tableName, [id, text, 0]))

    def removeEntry(self, id):
        self.__database.remove(self.__tableName, ['id'], [id])
        for e in self.__elements:
            if e.getId() == id:
                self.__elements.remove(e)
                return True
        return False

    def setText(self, id, text):
        col_name = 'text'
        self.__database.update(self.__tableName, id, [col_name], [text])
        for e in self.__elements:
            if e.getId() == id:
                e.setText(text)
                return True
        return False

    def changeState(self, id):
        for e in self.__elements:
            if e.getId() == id:
                self.__database.update(self.__tableName, id, ['state'], [e.changeState()])
                return True
        return False


