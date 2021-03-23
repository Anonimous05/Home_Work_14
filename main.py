import sqlite3

con = sqlite3.connect('db.sqlite3')

cursor = con.cursor()


class ORM:

    @classmethod
    def create_table(cls):
        cursor.execute(f"CREATE TABLE {cls.__name__.lower()} (id PRIMARY KEY, student_name TEXT, age INTEGER)")

    @classmethod
    def insert(cls, other):
        cursor.execute(f"INSERT INTO {cls.__name__.lower()} VALUES ({other.key}, '{other.name}', {other.age})")
        con.commit()

    @classmethod
    def update(cls, other):
        cursor.execute(f"UPDATE {cls.__name__.lower()} SET student_name='{other.name}', age={other.age} WHERE id={other.key}")
        con.commit()
        con.close()

    @classmethod
    def delete(cls, other):
        cursor.execute(f"DELETE from {cls.__name__.lower()} WHERE id={other.key}")
        con.commit()
        con.close()


class Students(ORM):
    def __init__(self, key, name, age):
        self.key = key
        self.name = name
        self.age = age


student = Students(4, "Don", 28)
student.delete(student)
con.close()
