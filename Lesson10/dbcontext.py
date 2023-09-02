import sqlite3 as sql
class DBContext:
    def __init__(self, database:str, timeout:float):
        self.DataBase = database
        self.TimeOut = timeout
    def Query(self, query:str):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
            connection.close()
        finally:
            connection.close()



