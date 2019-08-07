import sqlite3
class Database:
# we created a class for our functions so that we only need to make load, make
# cursor object, and close statement only once
# out code is shorter and looks better if all database manipulations use classes

# creating a database, function names should explain what each function does
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory(id INTEGER PRIMARY KEY,"
                         " name TEXT,"
                         " location TEXT,"
                         " quantity INTEGER,"
                         " id_name INTEGER)")
        self.conn.commit()

    def insert(self,name, location, quantity,id_name):
        self.cur.execute("INSERT INTO inventory VALUES(NULL,?,?,?,?)",(name, location, quantity,id_name))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT*FROM inventory")
        rows=self.cur.fetchall()
        return rows

    def search(self,name="", location="",quantity="",id_name=""):
        self.cur.execute("SELECT*FROM inventory WHERE name =? OR location =? OR quantity=? OR id_name=?", (name, location, quantity,id_name))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM inventory WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, name, location, quantity,id_name):
        self.cur.execute("UPDATE inventory SET name =?, location =?, quantity=?, id_name=? WHERE id=?", (name, location, quantity,id_name,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


