import pymysql

class DatabaseManager(object):
    __inst = None
    __connection = None

    @staticmethod
    def inst():
        if DatabaseManager.__inst == None:
            DatabaseManager.__inst = DatabaseManager()
        return DatabaseManager.__inst

    def __init__(self):
        self.__connection = pymysql.connect(host="localhost", user="root", passwd="fishkiller", db="todolist",
                                            use_unicode=True, charset="utf8", autocommit=True)

    def read_all(self, table):
        cur = self.__connection.cursor()
        cur.execute('Select * from ' + table + ';')
        return cur.fetchall()

    def read_columns(self, table, cols):
        fields = ','.join(map(str, cols))

        cur = self.__connection.cursor()
        cur.execute('select ' + fields + ' from ' + table + ';')
        return cur.fetchall()

    def update(self, table, id, cols, values):
        query = 'update ' + table + ' set '
        for i in range(len(cols)):
            s = cols[i] + '= "' + str(values[i]) + '",'
            query += s
        query = query[: -1]
        query += ' where id=' + str(id) + ';'
        cur = self.__connection.cursor()
        cur.execute(query)

    def insert(self, table, cols, values):
        query = 'insert into ' + table + '('
        query += ", ".join(cols) + ') values('
        for i in range(len(values)):
            values[i] = "'" + values[i] + "'"
        query += ", ".join(values) + ');'
        cur = self.__connection.cursor()
        cur.execute(query)
        return cur.lastrowid

    def remove(self, table, cols, values):
        query = 'delete from ' + table + ' where '
        for i in range(len(cols)):
            s = str(cols[i]) + ' = ' + str(values[i]) + ' and '
            query += s
        query = query[:-5]
        query += ';'
        cur = self.__connection.cursor()
        cur.execute(query)