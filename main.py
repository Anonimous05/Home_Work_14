import sqlite3

con = sqlite3.connect('db.sqlite3')

cursor = con.cursor()


class ORM:

    @classmethod
    def create_table(cls):
        cursor.execute(f"CREATE TABLE {cls.__name__.lower()} (id PRIMARY KEY, student_name TEXT, age INTEGER)")

    def insert(self):
        cursor.execute(f"INSERT INTO {self.__class__.__name__.lower()} VALUES ({self.key}, '{self.name}', {self.age})")
        con.commit()

    def update(self):
        cursor.execute(f"UPDATE {self.__class__.__name__.lower()} SET student_name='{self.name}', age={self.age} WHERE id={self.key}")
        con.commit()
        con.close()

    def delete(self):
        cursor.execute(f"DELETE from {self.__class__.__name__.lower()} WHERE id={self.key}")
        con.commit()
        con.close()


class Students(ORM):
    def __init__(self, key, name, age):
        self.key = key
        self.name = name
        self.age = age


student = Students(3, "Json Statham ahahahah", 48)
student.insert()
con.close()
