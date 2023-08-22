import sqlite3
con=sqlite3.connect("Unterricht.db")

cursor=con.cursor()


def table():
    cursor.execute("CREATE TABLE IF NOT EXISTS schuler(name TEXT, vorname TEXT, nummer INT, note INT)")
    con.commit()
  

def insert ():
    cursor.execute("INSERT INTO schuler VALUES ( 'Okan', 'Kuyucu', 12, 85)")
    con.commit()
    con.close()

table()
insert()